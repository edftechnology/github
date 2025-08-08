#!/bin/bash

# Specify the base branch (e.g., main, ita, ufabc)
BRANCH_BASE="main"

# Check and remove old lock file (if exists)
LOCK_FILE=".git/HEAD.lock"
if [ -f "$LOCK_FILE" ]; then
  echo "[INFO] Removing old lock file: $LOCK_FILE"
  rm -f "$LOCK_FILE"
fi

# Connect via SSH to avoid asking for the password every time
eval "$(ssh-agent -s)" >/dev/null
ssh-add ~/.ssh/id_rsa 2>/dev/null
ssh -T git@github.com

# Check for uncommitted local changes
if [[ -n $(git status --porcelain) ]]; then
  echo "[INFO] Local changes detected. Performing automatic commit..."
  git add .
  git commit -m "Automatic backup before switch"
else
  echo "[INFO] No local changes pending."
fi

# Switch to the base branch
echo "[INFO] Switching to base branch: $BRANCH_BASE"
git switch "$BRANCH_BASE"

# Update repository
git fetch --all
git pull origin "$BRANCH_BASE"

# Push recent changes
git push -u origin "$BRANCH_BASE"

# Get the most recent remote branch (excluding protected ones)
BRANCH_REMOTE=$(git for-each-ref --format="%(refname:short)" refs/remotes/origin/ \
  | grep -v '\->' \
  | grep -vE "origin/(HEAD|main|edf|iae|ita|ufabc)$" \
  | sed 's|^origin/||' \
  | tail -n 1)

# Check if a remote branch was found
if [[ -z "$BRANCH_REMOTE" ]]; then
  echo "[WARNING] No new remote branch found to merge. Exiting script."
  exit 0
fi

echo "[INFO] Remote branch to be merged: $BRANCH_REMOTE"

# Create local branch from remote
if git show-ref --verify --quiet "refs/heads/$BRANCH_REMOTE"; then
  echo "[INFO] Local branch '$BRANCH_REMOTE' already exists. Switching..."
  git switch "$BRANCH_REMOTE"
else
  echo "[INFO] Creating new local branch '$BRANCH_REMOTE' from 'origin/$BRANCH_REMOTE'"
  git checkout -b "$BRANCH_REMOTE" "origin/$BRANCH_REMOTE"
fi

# Make sure it is up to date
git pull

# Switch back to base and perform merge
git switch "$BRANCH_BASE"
echo "[INFO] Merging with '$BRANCH_REMOTE'"
git merge "$BRANCH_REMOTE" --no-edit || {
  echo "[ERROR] An error occurred during merge. Aborting."
  exit 1
}
git status --short
git push

# Clean up local branches that are not protected
echo "[INFO] Cleaning up non-protected local branches..."
git branch | grep -v -E '^\*|main$|edf$|iae$|ita$|ufabc$' | grep -q . && \
git branch | grep -v -E '^\*|main$|edf$|iae$|ita$|ufabc$' | xargs git branch -D

git branch | cat  # Show remaining local branches

# Delete remote branches that are not protected
echo "[INFO] Cleaning up non-protected remote branches..."
git remote prune origin
git branch -r | grep -v -E 'origin/(main|edf|iae|ita|ufabc)$' | sed 's|origin/||' \
  | xargs -I {} git push origin --delete {} || true

# Final confirmation
echo "[INFO] Script completed successfully."
git branch -r | cat
git status
