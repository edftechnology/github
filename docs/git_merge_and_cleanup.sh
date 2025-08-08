#!/bin/bash

# Especificar a branch base (ex: main, ita, ufabc)
BRANCH_BASE="main"

# Verifica e remove lock antigo (se existir)
LOCK_FILE=".git/HEAD.lock"
if [ -f "$LOCK_FILE" ]; then
  echo "[INFO] Removendo arquivo de lock antigo: $LOCK_FILE"
  rm -f "$LOCK_FILE"
fi

# Conectar via SSH sem pedir senha toda hora
eval "$(ssh-agent -s)" >/dev/null
ssh-add ~/.ssh/id_rsa 2>/dev/null
ssh -T git@github.com

# Verificar se ha mudancas locais nao commitadas
if [[ -n $(git status --porcelain) ]]; then
  echo "[INFO] Mudancas locais detectadas. Realizando commit automatico..."
  git add .
  git commit -m "Backup automatico antes do switch"
else
  echo "[INFO] Nenhuma mudanca local pendente."
fi

# Trocar para a branch base
echo "[INFO] Trocando para a branch base: $BRANCH_BASE"
git switch "$BRANCH_BASE"

# Atualizar repositório
git fetch --all
git pull origin "$BRANCH_BASE"

# Subir mudancas recentes
git push -u origin "$BRANCH_BASE"

# Obter a branch remota mais recente (excluindo protegidas)
BRANCH_REMOTE=$(git for-each-ref --format="%(refname:short)" refs/remotes/origin/ \
  | grep -v '\->' \
  | grep -vE "origin/(HEAD|main|edf|iae|ita|ufabc)$" \
  | sed 's|^origin/||' \
  | tail -n 1)

# Verificar se encontrou alguma branch
if [[ -z "$BRANCH_REMOTE" ]]; then
  echo "[AVISO] Nenhuma branch remota nova encontrada para mesclar. Encerrando script."
  exit 0
fi

echo "[INFO] Branch remota a ser mesclada: $BRANCH_REMOTE"

# Criar branch local a partir da remota
if git show-ref --verify --quiet "refs/heads/$BRANCH_REMOTE"; then
  echo "[INFO] Branch local '$BRANCH_REMOTE' ja existe. Fazendo checkout..."
  git switch "$BRANCH_REMOTE"
else
  echo "[INFO] Criando nova branch local '$BRANCH_REMOTE' a partir de 'origin/$BRANCH_REMOTE'"
  git checkout -b "$BRANCH_REMOTE" "origin/$BRANCH_REMOTE"
fi

# Garantir que esta atualizado
git pull

# Voltar para a base e fazer merge
git switch "$BRANCH_BASE"
echo "[INFO] Fazendo merge com '$BRANCH_REMOTE'"
git merge "$BRANCH_REMOTE" --no-edit || {
  echo "[ERRO] Ocorreu um erro durante o merge. Abortando."
  exit 1
}
git status --short
git push

# Limpar branches locais que nao sao protegidas
echo "[INFO] Limpando branches locais nao protegidas..."
git branch | grep -v -E '^\*|main$|edf$|iae$|ita$|ufabc$' | grep -q . && \
git branch | grep -v -E '^\*|main$|edf$|iae$|ita$|ufabc$' | xargs git branch -D

git branch | cat  # Mostrar branches locais restantes

# Deletar branches remotas nao protegidas
echo "[INFO] Limpando branches remotas nao protegidas..."
git remote prune origin
git branch -r | grep -v -E 'origin/(main|edf|iae|ita|ufabc)$' | sed 's|origin/||' \
  | xargs -I {} git push origin --delete {} || true

# Confirmacao final
echo "[INFO] Processo concluido com sucesso."
git branch -r | cat
git status
