#!/bin/bash

# Perguntar ao usuario qual a branch base (ex: main, ita, ufabc)
read -p "Enter the base branch name [default: main]: " BRANCH_BASE
BRANCH_BASE=${BRANCH_BASE:-main}

# Verifica e remove lock antigo (se existir)
LOCK_FILE=".git/HEAD.lock"
if [ -f "$LOCK_FILE" ]; then
  echo "[INFO] Removing old lock file: $LOCK_FILE"
  rm -f "$LOCK_FILE"
fi

# Conectar via SSH sem pedir senha toda hora
eval "$(ssh-agent -s)" >/dev/null
ssh-add ~/.ssh/id_rsa 2>/dev/null
ssh -T git@github.com

# Verificar se há mudanças locais não commitadas
if [[ -n $(git status --porcelain) ]]; then
  echo "[INFO] Local changes detected. Performing automatic commit..."
  git add .
  git commit -m "Automatic backup before switch"
else
  echo "[INFO] No local changes pending."
fi

# Trocar para a branch base
echo "[INFO] Switching to base branch: $BRANCH_BASE"
git switch "$BRANCH_BASE"

# Atualizar repositório
git fetch --all
git pull origin "$BRANCH_BASE"

# Subir mudanças recentes
git push -u origin "$BRANCH_BASE"

# Listar branches remotas não protegidas
echo "[INFO] Listing remote branches (excluding protected)..."
BRANCHES=($(git for-each-ref --format="%(refname:short)" refs/remotes/origin/ \
  | grep -v '\->' \
  | grep -vE "origin/.*(main|edf|iae|ita|ufabc).*" \
  | sed 's|^origin/||'))

if [[ ${#BRANCHES[@]} -eq 0 ]]; then
  echo "[WARNING] No new remote branches found to merge. Exiting script."
  exit 0
fi

echo
for i in "${!BRANCHES[@]}"; do
  echo "[$i] ${BRANCHES[$i]}"
done

echo
read -p "Enter the number of the branch to merge: " BRANCH_INDEX
BRANCH_REMOTE="${BRANCHES[$BRANCH_INDEX]}"

echo "[INFO] Remote branch to be merged: $BRANCH_REMOTE"

# Criar branch local a partir da remota
if git show-ref --verify --quiet "refs/heads/$BRANCH_REMOTE"; then
  echo "[INFO] Local branch '$BRANCH_REMOTE' already exists. Switching..."
  git switch "$BRANCH_REMOTE"
else
  echo "[INFO] Creating new local branch '$BRANCH_REMOTE' from 'origin/$BRANCH_REMOTE'"
  git checkout -b "$BRANCH_REMOTE" "origin/$BRANCH_REMOTE"
fi

# Garantir que está atualizado
git pull

# Voltar para a base e fazer merge
git switch "$BRANCH_BASE"
echo "[INFO] Merging with '$BRANCH_REMOTE'"
git merge "$BRANCH_REMOTE" --no-edit || {
  echo "[ERROR] An error occurred during merge. Aborting."
  exit 1
}
git status --short
git push

# Limpar branches locais que não são protegidas
echo "[INFO] Cleaning up non-protected local branches..."
git branch | grep -v -E '^\*|.*(main|edf|iae|ita|ufabc).*' | grep -q . && \
git branch | grep -v -E '^\*|.*(main|edf|iae|ita|ufabc).*' | xargs git branch -D

git branch | cat  # Mostrar branches locais restantes

# Deletar branches remotas não protegidas
echo "[INFO] Cleaning up non-protected remote branches..."
git remote prune origin
git branch -r | grep -v -E 'origin/.*(main|edf|iae|ita|ufabc).*' | sed 's|origin/||' \
  | xargs -I {} git push origin --delete {} || true

# Confirmação final
echo "[INFO] Script completed successfully."
git branch -r | cat
git status
