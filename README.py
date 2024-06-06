#!/usr/bin/env python
# coding: utf-8

# <!-- LOGOTIPO DO PROJETO -->
# <div style="display: flex; justify-content: center;">
#    <a href="https://github.com/edendenis/git">
#      <img src="figures/gold_edf_technology_logo_transparent_background_and_gold_name.png" alt="Logo" width="160" height="160">
#    </a>
# </div>
# 
# <h3 align="center">Configurar/Instalar/Usar o `Git` e descrição dos seus principais comandos</h3>
# 
# <!-- <div style="display: flex; justify-content: center;">
#   <a href="https://zenodo.org/doi/10.5281/zenodo.10668919">
#     <img src="https://zenodo.org/badge/758237447.svg" alt="DOI">
#   </a>
# </div> -->
# 
# <p align="center">
#  Neste documento estão contidos os principais comandos para configurar/instalar/usar o `Git`.
#  <br />
#  <a href="https://github.com/edendenis/git"><strong>Explore os documentos »</strong></a>
#  <br />
#  <br />
#  <a href="https://github.com/edendenis/git">Ver demonstração</a>
#  ·
#  <a href="https://github.com/edendenis/git">Relatar bug</a>
#  ·
#  <a href="https://github.com/edendenis/git">Solicitar recurso</a>
# </p>
# 

# # Configurar/Instalar/Usar o `Git` e descrição dos seus principais comandos
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos para configurar/instalar/usar o `Git`.
# 
# ## _Abstract_
# 
# _This document contains the main commands for configuring/installing/using the `Git`._
# 

# ## Descrição [2]
# 
# ### `Git`
# 
# O `Git` é um sistema de controle de versão distribuído amplamente utilizado para rastrear e gerenciar o código-fonte de projetos de desenvolvimento de software. Desenvolvido por Linus Torvalds, o criador do Linux, o `Git` é conhecido por sua eficiência, flexibilidade e capacidade de trabalhar tanto em projetos individuais quanto em equipes de desenvolvimento. Ele permite que os desenvolvedores acompanhem as alterações feitas no código, revertam para versões anteriores, colaborem em projetos e gerenciem conflitos de maneira eficaz. O `Git` também é suportado por várias plataformas de hospedagem de código, como o GitHub, o GitLab e o Bitbucket, o que o torna uma escolha central para o desenvolvimento colaborativo e a gestão de código-fonte em projetos de software.

# ## 1. Sobre os _branches_ do `Git` [1][2]
# 
# Ramos (`branches`) no `Git` são um recurso fundamental e poderoso do sistema de controle de versão `Git`. Um ramo em `Git` é um ponteiro leve e móvel para um `commit` específico. Quando você cria um novo ramo, permite que você se desvie da linha principal de desenvolvimento (geralmente o ramo "`master`" ou "`main`") e trabalhe em novas funcionalidades, correções de bugs ou experimentos sem afetar o código principal.
# 
# Aqui estão alguns conceitos-chave relacionados aos ramos (branches) do `Git`:
# 
# 1. **Ramo Master/Principal:** O ramo padrão em um repositório `Git` é frequentemente chamado de "master" ou "main". Esse ramo representa o código estável e pronto para produção. Geralmente é a base a partir da qual outros ramos são criados.
# 
# 2. **Criando um Ramo:** Você pode criar um novo ramo no `Git` usando o comando `git branch` seguido pelo nome do ramo. Por exemplo, para criar um novo ramo chamado "feature-branch", você usaria: `git branch feature-branch`.
# 
# 3. **Alternando Entre Ramos:** Para mudar para um ramo diferente, você usa o comando `git checkout` seguido do nome do ramo. A partir do `Git` 2.23, você também pode usar `git switch` para esse propósito. Por exemplo: `git checkout feature-branch` ou `git switch feature-branch`.
# 
# 4. **Criando e Alternando em um Único Passo:** Você pode criar e mudar para um novo ramo simultaneamente usando a opção `-b com git checkout` ou `git switch`. Por exemplo: `git checkout -b new-feature` ou `git switch -c new-feature`.
# 
# 5. **Visualizando Ramos:** O comando `git branch` lista todos os ramos no repositório. O ramo atual é marcado com um asterisco (*).
# 
# 6. **Mesclando Ramos:** Depois de terminar o trabalho em um ramo de funcionalidade, você pode mesclá-lo de volta ao ramo principal (por exemplo, master/main). Isso combina as mudanças do ramo de funcionalidade no ramo principal. Você pode usar `git merge` para fazer isso.
# 
# 7. **Resolvendo Conflitos:** Ao mesclar ramos, se houver conflitos (ou seja, mudanças na mesma parte do código), o `Git` pedirá que você resolva os conflitos manualmente.
# 
# 8. **Fluxos de Trabalho com Ramos:** O uso de ramos no `Git` possibilita vários fluxos de trabalho, como o "Feature Branch Workflow", o "Gitflow Workflow" e o "`Git` Forking Workflow", entre outros. Esses fluxos de trabalho ajudam as equipes a colaborar de forma eficaz e gerenciar o código de maneira eficiente.
# 
# 9. **Ramos Remotos:** Ramos remotos representam ramos em um repositório remoto (por exemplo, no GitHub, GitLab ou Bitbucket). Você pode enviar seus ramos locais para um repositório remoto e trazer ramos remotos para o seu repositório local.
# 
# O uso de ramos no `Git` permite que os desenvolvedores trabalhem colaborativamente em diferentes partes do projeto simultaneamente. Ele facilita o isolamento do código, a experimentação e a capacidade de trabalhar em várias funcionalidades ao mesmo tempo. Ramos são um conceito fundamental no `Git` que promove a organização do código, a manutenibilidade e o trabalho em equipe.

# ## 2. Configurar/Instalar/usar o `Git` [1]
# 
# ## 2.1 Configurar/Instalar/usar o `Git` no `Linux Ubuntu`
# 
# Para configurar/instalar o `Git` no `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. No `Terminal Emulator` do Sistema Operacional (SO), executar o comando: `sudo apt install git-all -y`

# ### 2.2 Configurar/Instalar/usar o `Git` no `Windows` a partir da fonte
# 
# Para instalar o `git-all` no `Windows` usando o `PowerShell`, você seguirá basicamente dois passos: primeiro, baixar o instalador do `Git`, e depois, executá-lo. Aqui estão as instruções detalhadas:
# 
# 1. **Baixar o Instalador do Git:** Abra o navegador e vá até o site oficial do `Git`: `https://git-scm.com/`.
# 
#     - Baixe a versão mais recente do `Git` para `Windows`. O arquivo será um instalador .`exe`.
# 
# 2. **Instalar o `Git` usando o `PowerShell`:**
# 
#     - Abra o `PowerShell` como administrador. Isso é importante para garantir que você tenha as permissões necessárias para instalar programas.
# 
#     - Navegue até o diretório onde o instalador do `Git` foi baixado. Por exemplo, se o arquivo foi baixado na pasta de `Downloads`, você pode usar o comando: `cd ~\Downloads`
# 
#     - Execute o instalador do `Git`. Se o arquivo se chamar `Git-2.31.1-64-bit.exe`, por exemplo, você digitará: `.\Git-2.31.1-64-bit.exe`
#     
#     O nome do arquivo varia de acordo com a versão baixada.
# 
#     - Siga as instruções na tela para completar a instalação. Durante a instalação, você pode aceitar as configurações padrão ou personalizá-las conforme sua necessidade.
# 
# 3. Depois de concluir a instalação, você pode verificar se o `Git` foi instalado corretamente abrindo um novo terminal do `PowerShell` e digitando: `git --version`
# 
#     Isso deve retornar a versão do Git que foi instalada.

# ## 2.3 Criar chave Secure SHell `ssh` para a conta do usuário [4][5]
# 
# ### 2.3.1 Verificar se foi liberado o acesso ao `Git`
# 
# Antes de seguir os passos de uma das Seções abaixo (`Linux` e/ou `Windows`), confirmar com um dos administradores do `Git` se foi liberado o acesso para a sua conta de e-mail. Se não, solicitar o acesso antes de prosseguir com o passo a passo de uma Seções abaix (`Linux` e/ou `Windows`). 
# 
# ### 2.3.2 `Linux Ubuntu`
# 
# Para gerar uma chave SSH no `Linux Ubuntu`, você pode seguir os passos abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. No `Terminal Emulator`, digite o seguinte comando para gerar um novo par de chaves SSH: `ssh-keygen -t rsa`
# 
# 4. O comando acima irá gerar um par de chaves RSA (Rivest-Shamir-Adleman). Você também pode usar outros algoritmos de chave, como `dsa` ou `ecdsa`, se preferir. Pressione `Enter` para aceitar o local padrão do arquivo da chave.
# 
# 5. Em seguida, você será solicitado a inserir uma frase secreta (passphrase) para proteger sua chave. É recomendável usar uma senha forte e exclusiva para aumentar a segurança. Você pode pressionar `Enter` para deixar a frase secreta em branco, mas isso diminuirá a segurança da sua chave.
# 
# 6. Após fornecer a frase secreta ou pressionar `Enter`, o comando `ssh-keygen` irá gerar duas chaves: uma chave privada (`id_rsa`) e uma chave pública (`id_rsa.pub`). A chave privada deve ser mantida em segredo e protegida com a frase secreta, enquanto a chave pública pode ser compartilhada.
# 
# 7. Por padrão, as chaves SSH são salvas no diretório `~/.ssh/`. Você pode listar o conteúdo desse diretório usando o comando: `ls ~/.ssh/`
# 
# 8. Agora você pode usar sua chave pública (`id_rsa.pub`) para autenticar em servidores remotos. Você pode copiar a chave pública para o servidor remoto usando o comando `ssh-copy-id`. Por exemplo: `ssh-copy-id -i ~/.ssh/id_rsa.pub usuário@servidor`
# 
#     Substitua `"usuário"` pelo seu nome de usuário no servidor remoto e `"servidor"` pelo endereço IP ou nome do servidor remoto. Você será solicitado a inserir a senha do usuário no servidor remoto.
# 
#     Depois de copiar a chave pública, você poderá fazer login no servidor remoto sem precisar digitar a senha toda vez, desde que a chave privada esteja presente no sistema local e a frase secreta (se fornecida) esteja correta.
# 
#     Lembre-se de proteger sua chave privada e evitar compartilhá-la com outras pessoas. É recomendável usar autenticação por chave SSH em vez de senhas, pois oferece uma camada adicional de segurança.
# 
# #### Configurar o `Git` para usar SSH
# 
# 1. **Altere o URL remoto do seu repositório para usar SSH**: `git remote set-url origin git@github.com:edendenis/<nome_do_projeto>.git`

# ### 2.3.3 `Windows` [5]
# 
# Para gerar uma chave SSH no Windows para uso no `Git`, você pode seguir as etapas abaixo:
# 
# 1. Verifique se você tem o `Git` instalado no seu computador. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do `Git`: https://git-scm.com/downloads
# 
# 2. Abra o `Git` Bash. Você pode fazer isso clicando com o botão direito do mouse em qualquer diretório e selecionando a opção `"Git Bash Here"` no menu de contexto.
# 
# 3. No `Git Bash`, digite o seguinte comando para gerar uma nova chave SSH:
# 
#     `ssh-keygen -t rsa -C "seu_email@exemplo.com"` (`@gitlab.com`)
# 
#     Certifique-se de substituir `seu_email@exemplo.com` pelo seu endereço de e-mail associado à sua conta do `Git`. Você pode deixar a senha em branco pressionando Enter duas vezes.
# 
# 4. Será solicitado que você forneça um local para salvar a chave. Você pode simplesmente pressionar Enter para aceitar o local padrão (geralmente `C:\Usuários\SeuNome\.ssh\id_rsa`).
#     
# 5. O comando irá gerar a chave SSH pública e privada. Por padrão, a chave pública será salva como `id_rsa.pub`.
# 
# 6. Agora, você precisa adicionar a chave SSH pública à sua conta do GitLab. Abra o GitLab no seu navegador e faça login na sua conta.
# 
# 7. No canto superior direito da página, clique na sua foto de perfil e vá para `Settings` (Configurações) no menu suspenso.
# 
# 8. No menu lateral esquerdo, clique em `SSH Keys` (Chaves SSH).
# 
# 9. No campo `Key`, abra o arquivo `id_rsa.pub`` (ou qualquer nome que você tenha dado à sua chave pública) que você gerou anteriormente. Copie todo o conteúdo do arquivo e cole no campo "Key" no GitLab.
# 
# 10. Dê um nome para a chave, por exemplo, `Meu Computador` e clique em `Add Key` (Adicionar chave).
# 
# Agora você gerou e adicionou com sucesso uma chave SSH para uso no GitLab. Você poderá usar essa chave para autenticar suas operações do GitLab usando o `Git` no Windows.
# 
# Depois de copiar a chave pública, você poderá fazer login no servidor remoto sem precisar digitar a senha toda vez, desde que a chave privada esteja presente no sistema local e a frase secreta (se fornecida) esteja correta.
# 
# Lembre-se de proteger sua chave privada e evitar compartilhá-la com outras pessoas. É recomendável usar autenticação por chave SSH em vez de senhas, pois oferece uma camada adicional de segurança.

# ### 2.4 Comando `git init`
# 
# O comando `git init` é usado para iniciar um novo repositório `Git` em um diretório. Quando você executa este comando em um diretório vazio ou existente, ele cria um repositório `Git` local, que é um local onde você pode armazenar e gerenciar seu código fonte e seu histórico de alterações. Aqui está uma explicação mais detalhada em código e comentários:
# 
# 1. Inicializa um novo repositório Git no diretório atual: `git init`
# 
#     Este comando cria um diretório oculto chamado `.git` na pasta onde você executou o `git init`. É dentro deste diretório `.git` que o `Git` armazena todas as informações sobre o repositório, incluindo o histórico de `commits`, as configurações e outras informações relacionadas ao controle de versão.
# 
# #### 2.4.1 Configurar o `branch` padrão ou alterar o `branch`
# 
# Usando `master` como nome do `branch` inicial. Este nome de branch padrão está sujeito a alterações. Para configurar o nome inicial da filial a ser usada em todos os seus novos repositórios, que suprimirão este aviso, chame `git config --global init.defaultBranch <nome>`, você pode alterar o `branch` para `develop` com o seguinte comando: `git config --global init.defaultBranch develop` 
# 
# Os nomes comumente escolhidos em vez de `master` são `main`, `trunk` e `development`. O branch recém-criado pode ser renomeado através deste comando: `git branch -m <nome>`

# ### 2.5 Clonar o repositório do `Git`
# 
# 1. No Terminal do Sistema Operacional (SO), executar o comando: `git clone -b <nome_da_branch> <URL_da_branch>`, por exemplo, como caso real: `git clone -b develop git@gitlab.com:iae-apr/proplib.git` 

# ### 2.6 Comando `git checkout`
# 
# 1. No Terminal do Sistema Operacional (SO), executar o comando: `git checkout` para verificar qual a `branch` está selecionada;
# 2. Como a `branch` de desenvolvimento é a `develop`, é conveniente, selecioná-la caso não esteja selecionada, para isso, digitar: `git checkout`.

# #### 2.6.1 Comando `git checkout <codigo_da_hash>` [7]
# 
# O comando `git checkout <codigo_da_hash>` (para o caso real: git checkout a3636068`) é usado no `Git` para mudar o estado do repositório para o estado em que estava no momento do commit especificado pelo hash `a3636068`. Aqui está uma explicação detalhada:
# 
# - **`git checkout`:** Este é um comando versátil usado no `Git` para trocar de branches ou restaurar arquivos da árvore de trabalho.
# 
# - **`a3636068`:** Este é um exemplo de um hash de commit. Os hashes são identificadores únicos para cada `commit` no histórico do `Git`. Ao especificar um `hash` de `commit`, você está indicando exatamente qual commit o `Git` deve usar como referência.
# 
# Quando você executa `git checkout a3636068`, o seguinte acontece:
# 
# 1. **Mudança de Estado:** O repositório muda para o estado em que estava no momento do commit `a3636068`. Isso significa que todos os arquivos no diretório de trabalho serão revertidos para como estavam no momento daquele commit.
# 
# 2. **Detached HEAD State:** Você entrará no estado "Detached HEAD". Isso significa que você não estará mais em uma branch específica. Qualquer novo commit criado a partir desse ponto estará "flutuando" e não pertencerá a nenhuma branch, a menos que você crie uma nova branch a partir deste ponto.
# 
# 3. **Exploração e Testes:** Este comando é útil para explorar o estado do repositório em um ponto específico no passado, verificar alterações antigas, realizar testes, entre outros.
# 
# É importante notar que ao fazer mudanças enquanto estiver em um estado "Detached HEAD", você deve criar uma nova branch para preservar essas mudanças, pois se retornar para uma branch diferente sem fazer isso, as mudanças feitas serão perdidas. 
# 

# ## 2.7 Comando `git status` [1][2]
# 
# O comando `git status` é um dos comandos mais utilizados no `Git`, e é usado para verificar o estado do repositório `Git` local em relação ao seu diretório de trabalho e à área de preparação (também conhecida como "staging area"), ver Figura (1).
# 
# Quando você executa `git status`, o `Git` informa sobre algumas informações importantes:
# 
# 1. **Branch Atual:** Mostra em qual ramificação (branch) você está trabalhando atualmente.
# 
# 2. **Changes not staged for commit:** Lista de arquivos modificados no diretório de trabalho, mas ainda não adicionados à área de preparação (staging area) para um novo commit. Essas mudanças não serão incluídas no próximo commit, a menos que você as adicione manualmente usando o comando git add.
# 
# 3. **Changes to be committed:** Lista de arquivos que foram adicionados à área de preparação (staging area) e estão prontos para serem incluídos no próximo commit. Essas mudanças serão efetivadas no repositório após o comando git commit.
# 
# 4. **Untracked files:** Lista de arquivos que o `Git` não está rastreando atualmente. Isso significa que o `Git` não está ciente de quaisquer alterações nesses arquivos. Para começar a rastreá-los, você deve adicioná-los à área de preparação usando o comando git add.
# 
# O resultado do comando git status é uma visão geral do estado do seu repositório, mostrando o que foi modificado, o que está preparado para o próximo commit e quais arquivos ainda não estão sendo rastreados pelo `Git`.
# 
# É uma boa prática executar o comando git status frequentemente para se manter atualizado sobre o estado do seu repositório e garantir que você esteja preparado para criar commits com as alterações corretas.

# <div align="center">
#     <img src="figures/working_tree_staging_area_and_git_directory.png" alt="Minha Imagem" />
#     <p>Figura. 1: Árvore de trabalho, área de preparação e diretório do `Git`. [3]</p>
# </div>

# # 2.8 Comando `git add` [1][2]
# 
# O comando `git add` é usado no `Git` para adicionar alterações feitas nos arquivos do diretório de trabalho à área de preparação (staging area). A área de preparação é uma etapa intermediária entre o diretório de trabalho e o próximo `commit` que você irá criar. Quando você executa `git add`, você está instruindo o `Git` a incluir as alterações específicas dos arquivos selecionados na próxima confirmação (`commit`).
# 
# Aqui estão alguns detalhes sobre o funcionamento do comando `git add`:
# 
# - **Adicionar Alterações Específicas:** O comando `git add` permite que você selecione quais alterações de arquivos você deseja incluir na área de preparação. Isso significa que você pode escolher quais mudanças serão incluídas no próximo `commit` e quais não serão.
# 
# - **Sintaxe Básica:** Para adicionar alterações em um arquivo específico, você pode usar o comando `git add nome_do_arquivo`. Por exemplo, para adicionar as alterações do arquivo "app.py", você usaria: `git add app.py`.
# 
# - **Adicionar Todas as Alterações:** Se você quiser adicionar todas as alterações de todos os arquivos que foram modificados no diretório de trabalho, você pode usar o comando `git add .` (o ponto faz parte do comando). O ponto `.` representa todos os arquivos modificados no diretório atual.
# 
# - **Adicionar em Lotes:** Além disso, você pode adicionar alterações de vários arquivos em um único commit, selecionando-os por padrão ou utilizando curingas. Por exemplo: `git add *.py` adiciona todas as alterações de arquivos JavaScript no diretório atual.
# 
# - **Verificar a Área de Preparação:** Para verificar quais alterações estão na área de preparação, você pode usar o comando `git status`. As alterações listadas sob `"Changes to be committed"` são as que serão incluídas no próximo `commit` após usar `git add`.
# 
# - **Adicionar todas as alterações listadas em `"Changes not staged for commit"`**: Para adicionar todas as alterações listadas em "Changes not staged for commit", você pode usar o seguinte comando: `git add -u`
# 
# - **Desfazer `git add`:** Se você acidentalmente adicionar alterações erradas ou quiser remover uma alteração da área de preparação, você pode usar o comando `git reset HEAD <nome_do_arquivo>` para remover o arquivo da área de preparação. Isso mantém as alterações no diretório de trabalho sem incluí-las no próximo `commit`.
# 
# **ATENÇÂO:** Lembre-se de que após usar o comando `git add` para adicionar as alterações à área de preparação, você ainda precisará criar um `commit` usando o comando `git commit` para tornar as alterações parte do histórico do repositório.

# ### 2.8.2 Editar o `git commit`
# 
# Para editar um `git commit` já salvo, você pode seguir os seguintes passos:
# 
# 1. **Abrir um Terminal:** Primeiro, você precisa de um terminal onde possa executar comandos Git.
# 
# 2. **Navegar até o Repositório:** Use o comando cd para navegar até a pasta do seu repositório Git.
# 
# 3. **Usar o Comando `git rebase`:**
# 
#     - Para editar o último `commit`, você pode usar `git commit --amend`. Isso abrirá um editor de texto onde você pode editar a mensagem do `commit`.
# 
#     - Se o `commit` que você quer editar não for o último, você precisará usar o `git rebase`. Por exemplo, se você quiser editar um `commit` que está três `commits` atrás, você usaria `git rebase -i HEAD~3`. Isso abrirá uma lista dos últimos três `commits` no seu editor de texto padrão.
# 

# #### 2.8.2 Comando `git reset HEAD <nome_do_arquivo>` [9]
# 
# Para remover arquivos do estado "Changes to be committed" no `Git`, você pode usar o comando `git reset`. Este comando irá desfazer a adição dos arquivos à área de `staging` (também conhecida como `index`), retornando-os para o estado `"Changes not staged for commit"`.
# 
# 1. Aqui está um exemplo de como usar o comando: `git reset <nome_do_arquivo>`
# 
# Se você quiser remover todos os arquivos da área de staging, pode usar o comando sem especificar um arquivo: `git reset`
#     
#     Isso irá desfazer a adição de todos os arquivos que estão atualmente na área de `staging`. Note que isso não irá modificar os arquivos em si, apenas remove a marcação deles como prontos para `commit`. As alterações feitas nos arquivos permanecerão intactas.
# 

# ## 3. Outros comandos
# 
# ### 3.1 Comando `git diff` [1][2]
# 
# Para visualizar as diferenças entre o diretório de trabalho (_working directory_) e a área de preparação (_staging area_), você pode usar o comando `git diff`. Esse comando compara o estado atual dos arquivos no diretório de trabalho com as alterações que foram adicionadas à área de preparação, mas ainda não foram efetivadas em um `commit`.
# 
# Aqui estão algumas formas de usar o comando `git diff` para visualizar as diferenças:
# 
# 1. **Visualizar a diferença para arquivos modificados:** Para ver a diferença nos arquivos que foram modificados no diretório de trabalho, mas ainda não foram adicionados à área de preparação, você pode simplesmente executar o comando `git diff`. Isso mostrará as alterações lado a lado.: `git diff`
# 
# 
# 2. **Visualizar a diferença para arquivos adicionados à área de preparação:** Se você quiser ver as alterações dos arquivos que já foram adicionados à área de preparação (_staging area_), use o seguinte comando: `git diff --staged`
# 
# 
# 3. **Visualizar a diferença para um arquivo específico:** Se você quiser visualizar as diferenças apenas para um arquivo específico, basta fornecer o nome do arquivo após o comando `git diff`: `git diff nome_do_arquivo`
# 
# 
# 4. **Visualizar a diferença para um arquivo específico adicionado à área de preparação:** Para visualizar as diferenças de um arquivo específico que já foi adicionado à área de preparação, você pode usar o mesmo comando anterior com a opção `--staged`: `git diff --staged nome_do_arquivo`
# 
# 
# 5. **Visualizar a diferença resumida (por linhas):** Você também pode usar a opção `-U` para exibir um número específico de linhas ao redor das alterações: `git diff -U3`
# 
# O número `3` no exemplo acima indica que o `Git` exibirá três linhas de contexto ao redor de cada alteração.
# 
# O comando `git diff` é uma ferramenta muito útil para revisar as alterações antes de efetivar um commit, permitindo que você verifique quais modificações serão incluídas no próximo commit e ajuda a evitar possíveis erros ou problemas no histórico do repositório.

# #### 3.1.1 Configurar o `git diff` para **NÃO** apontar mudanças nas informações de células colapsadas ou expandidas em notebooks do Jupyter
# 
# Para evitar que o `git diff` aponte mudanças nas informações de células colapsadas ou expandidas em notebooks do Jupyter, você pode usar um filtro de difusão do `git` que ignore as mudanças em metadados específicos.
# 
# Aqui está um passo a passo de como configurar isso:
# 
# 1. **Crie um script de filtro Git:** Crie um script Python que remova os metadados que você não quer acompanhar. Por exemplo, crie um arquivo chamado `filter_nb_metadata.py` e adicione o seguinte código:
# 
#     ```
#     #!/usr/bin/env python
#     import sys
#     import json
# 
#     nb = json.load(sys.stdin)
#     for cell in nb['cells']:
#         if 'metadata' in cell:
#             cell['metadata'] = {k: v for k, v in cell['metadata'].items() if k != 'jp-MarkdownHeadingCollapsed'}
# 
#     json.dump(nb, sys.stdout, sort_keys=True, indent=1, ensure_ascii=False)
#     ```
# 
# 2. Não esqueça de tornar o script executável com o comando: `chmod +x filter_nb_metadata.py`
# 
#     Se precisar use o `sudo` no comando acima, ou seja: `sudo +x filter_nb_metadata.py`
# 
#     2.1 Para confirmar se o script se tornou executável, verifique as permissões do arquivo com o comando: `ls -l filter_nb_metadata.py`
# 
#     Você deve ver algo como `-rwxr-xr-x` para o seu usuário. Se não for esse o caso, você precisará alterar as permissões com:
#     
# 3. **Adicione o script ao seu repositório `Git` como um atributo:** Crie o arquivo `.gitattributes` no seu repositório no seu repositório com o comando: `nano .gitattributes`
#     
#     Se precisar use o `sudo` no comando acima, ou seja: `sudo nano .gitattributes`
# 
# 4. Adicione a(s) linha(s) dentro do arquivo `.gitattributes`, como segue:
# 
#     ```
#     #!/usr/bin/env python3
#     *.ipynb filter=nbmetadata
#     ```
# 
# 5. **Configure o filtro `Git`:** Configure o `Git` para usar o script como filtro para arquivos `.ipynb`:
# 
#     ```
#     git config filter.nbmetadata.clean './filter_nb_metadata.py'
#     git config filter.nbmetadata.smudge cat
#     ```
# 
# 6. **(Opcional) Reaplique os filtros aos seus arquivos:** Para aplicar o filtro aos arquivos existentes, você pode usar: `git add --renormalize .`
# 
# Agora, quando você usar `git diff`, o `Git` usará seu script de filtro para limpar (clean) os notebooks antes de compará-los, efetivamente ignorando as mudanças nos metadados que você especificou. Isso significa que as informações de células colapsadas ou expandidas não aparecerão mais no `diff`.

# ## 4. Como puxar as atualizações para o repositório local
# 
# ### 4.1 Comando `git fetch` [1][2]
# 
# O comando `git fetch` é usado no sistema de controle de versão `Git` para buscar atualizações de um repositório remoto para o seu repositório local. No entanto, o `git fetch` não integra automaticamente as mudanças em seu código local; em vez disso, ele traz as alterações mais recentes do repositório remoto para que você possa visualizá-las e decidir como deseja proceder.
# 
# Quando você executa `git fetch`, o `Git` faz o seguinte:
# 
# 1. Verifica quaisquer alterações novas nos ramos remotos que você acompanha;
# 
# 2. Atualiza as referências remotas (por exemplo, os ramos remotos como `origin/master` ou `origin/main`) para apontar para as posições mais recentes nos ramos remotos correspondentes;
# 
# 3. Baixa as alterações (`commits`) associadas a essas referências atualizadas, mas não as mescla automaticamente com seus ramos locais.
# 
# 4. Isso é útil porque você pode visualizar as mudanças que foram feitas remotamente antes de decidir como incorporá-las ao seu trabalho local. Você pode examinar os `commits`, comparar ramos, revisar alterações e, em seguida, optar por usar o `git merge` ou `git rebase` para trazer as alterações locais e remotas juntas.
# 
#     4.1 Opções Adicionais:
# 
#     4.1.1 **Pular o Commit:** Se você decidir que um commit específico que está causando conflitos não precisa ser aplicado, você pode pular o `commit` com: g`it rebase --skip`
#     
#     Isso é útil se o c`ommit` contém mudanças que já não são relevantes ou se resolver o conflito é muito complicado e você tem certeza de que omitir as mudanças não afetará negativamente seu projeto.
# 
# Abortar o Rebase: Se você achar que o rebase está muito complicado ou se você começou por engano, você pode abortar o processo de rebase e retornar ao estado anterior com git rebase --abort.
# 
# Em resumo, `git fetch` é uma maneira de manter-se atualizado com o estado do repositório remoto sem mesclar automaticamente as mudanças em seu trabalho local. Isso dá a você mais controle sobre como integrar as alterações e evita possíveis conflitos indesejados.
# 
# #### 4.1.1 Comando `git pull`
# 
# Aqui está uma explicação do comando `git pull` em código e comentários:
# 
# 1. Busca as atualizações do repositório remoto e mescla-as na ramificação local: `git pull`
#     
#     Quando você executa `git pull`, o `Git` faz o seguinte:
# 
#     - **`git stash`:** O comando `git stash` é usado para temporariamente salvar (ou "guardar") as mudanças em seu diretório de trabalho que ainda não foram commitadas em um estado chamado de `stash`. Isso pode ser útil quando você está trabalhando em uma determinada ramificação, mas precisa alternar para outra ramificação ou realizar alguma outra tarefa que exija um diretório de trabalho limpo, ver Seção Comando `git stash`;
# 
#     - **`git fetch`:** Ele busca todas as atualizações do repositório remoto, incluindo todas as novas ramificações, `commits` e outras referências que podem ter sido adicionadas ao repositório remoto desde a sua última sincronização;
# 
#     - **`git merge` (ou `git rebase`, dependendo das configurações):** Após buscar as atualizações, o `Git` combina automaticamente as mudanças do repositório remoto com a sua ramificação local atual. Se você estiver usando o `git merge`, ele criará um novo `commit` de `merge` para incorporar as alterações do repositório remoto na sua ramificação. Se você estiver usando o `git rebase`, ele reaplicará seus `commits` locais no topo das atualizações do repositório remoto, criando uma linha de tempo mais linear.
# 
# O `git pull` é útil quando você deseja manter seu repositório local sincronizado com as mudanças feitas por outras pessoas no repositório remoto. Ele ajuda a atualizar sua ramificação local para refletir o estado atual do repositório remoto.
# 
# Lembre-se de que, ao usar o `git pull`, você pode encontrar conflitos se suas alterações locais entrarem em conflito com as alterações do repositório remoto. Nesse caso, você precisará resolvê-los manualmente antes de poder concluir o `git pull`.

# ### 4.2 Comando `git log` [4]
# 
# O comando `git log` é usado para exibir o histórico de commits em um repositório `Git`. Ele mostra informações detalhadas sobre os commits, incluindo o hash do commit, autor, data e hora, e a mensagem associada ao commit. Aqui está uma explicação mais detalhada de como o comando funciona: `git log`
# 
# Ao executar o comando `git log` sem argumentos adicionais, você verá uma lista de todos os commits no ramo atual (aquele em que você está atualmente). Cada entrada no registro do `git log`` representa um commit e inclui as seguintes informações:
# 
# - **Hash do Commit:** Um identificador exclusivo (geralmente em formato hexadecimal) que identifica de forma única o commit.
# 
# - **Autor:** O nome e o endereço de e-mail do autor do commit.
# 
# - **Data e Hora:** A data e a hora em que o commit foi criado.
# 
# - **Mensagem do Commit:** A mensagem descritiva associada ao commit, que geralmente explica as alterações feitas no commit.
# 
# O comando `git log` exibe os commits em ordem cronológica reversa, com o commit mais recente listado no topo.
# 
# Este comando é útil para visualizar o histórico de desenvolvimento do seu projeto, permitindo que você acompanhe quem fez quais alterações e quando essas alterações foram feitas. Você também pode usar várias opções e argumentos adicionais com o "git log" para personalizar a saída, como limitar o número de commits exibidos, filtrar por autor, data ou mensagem de commit, e muito mais.

# ### 4.2.1 Comando `git log --oneline` [7]
# 
# O comando `git log --oneline` no `Git` é utilizado para exibir um histórico conciso dos commits no repositório. Este comando apresenta cada commit em uma única linha, tornando mais fácil e rápido de visualizar as mudanças ao longo do tempo. Aqui está o que ele faz:
# 
# - **`git log`:** Este é o comando básico para exibir o histórico de commits em um repositório `Git`.
# 
# - **`--oneline`:** Esta opção modifica a saída do comando git log para mostrar cada commit em uma única linha. Isso inclui o identificador do commit (hash) abreviado e a mensagem do commit.
# O resultado é uma visão compacta e fácil de ler do histórico do repositório, útil para obter uma rápida visão geral das mudanças recentes.

# ### 4.2.2 Consultar os últimos `commits`
# 
# Para consultar os últimos `commits` no Git através do terminal, você pode utilizar o comando git log. Aqui estão algumas das formas mais comuns de usar o git log para visualizar o histórico de `commits`:
# 
# 1. **Visualizar uma Lista Simples de Commits:** `git log`
# 
#     Este comando mostrará uma lista detalhada dos `commits`, incluindo o autor, a data e a mensagem de cada commit.
# 
# 2. **Limitar o Número de Commits Mostrados:** `git log -n <número>`
# 
#     Substitua <número> pelo número de `commits` que você deseja ver. Por exemplo, `git log -n 5` mostrará os últimos cinco `commits`.
# 
# 3. **Mostrar Commits em uma Linha:** `git log --oneline`
# 
#     Esta opção exibe cada `commit` em uma única linha, mostrando apenas o identificador do `commit` (`hash`) e a mensagem do `commit`.
# 
# 4. **Mostrar Commits com Estatísticas de Mudanças:** `git log --stat`
# 
#     Além da informação normal, isso mostrará estatísticas de mudança para cada `commit`, como quantos arquivos foram alterados e o número de linhas adicionadas ou removidas.
# 
# 5. **Mostrar um Gráfico dos Branches e Merges:**  `git log --graph`
# 
#     Isso adiciona um gráfico ASCII ao lado das mensagens de `commit`, mostrando a estrutura de `branches` e `merges`.
# 
# 6. **Filtrar Commits por Autor:** `git log --author="Nome do Autor"`
# 
#     Substitua "Nome do Autor" pelo nome do autor para ver apenas os `commits` feitos por essa pessoa.
# 
# 7. **Mostrar Commits Desde Uma Data Específica:**  `git log --since="2023-01-01"`
# 
#     Substitua "2023-01-01" pela data desejada para ver `commits` desde aquela data.
# 
# 8. **Mostrar Commits Antes de Uma Data Específica:** `git log --until="2023-01-01"`
# 
#     Similar ao comando `--since`, mas mostra `commits` anteriores à data especificada.
# 
# Esses são apenas alguns exemplos de como você pode usar `git log` para explorar o histórico de `commits`. O Git oferece muitas outras opções e filtros que podem ser aplicados ao comando `git log` para personalizar a saída de acordo com suas necessidades.
# 

# ### 4.3 Comando `git push` [1][2]
# 
# O comando `git push` é usado para enviar as alterações locais do seu repositório `Git` para um repositório remoto, como GitHub, GitLab, Bitbucket ou outro servidor `Git`. Quando você faz `git push`, você está enviando os commits que você criou no seu repositório local para o repositório remoto, tornando as suas alterações disponíveis para outras pessoas que trabalham no mesmo projeto.
# 
# A sintaxe básica do comando `git push` é a seguinte:
# 
# ```
# git push --set-upstream <remote_name> <branch_name>
# ```
# 
# Onde:
# 
# `--set-upstream`: O argumento `--set-upstream` (ou sua forma abreviada -u) no comando `git push` é usado para configurar a ramificação local para rastrear uma ramificação remota após a realização bem-sucedida do push. Aqui está uma explicação mais detalhada:
# 
# `<remote_name>` é o nome do repositório remoto para o qual você deseja enviar suas alterações. Por padrão, o repositório remoto principal é chamado de "origin", mas você pode configurar outros repositórios remotos, se necessário.
# 
# `<branch_name>` é o nome da ramificação (branch) que você deseja enviar para o repositório remoto. Por exemplo, se você estiver trabalhando na ramificação "feature-branch" e quiser enviar suas alterações para o repositório remoto, você usaria `git push origin feature-branch`.
# 
# **ATENÇÃO:** Antes de fazer `git push`, é importante garantir que você tenha concluído as etapas anteriores corretamente:
# 
# 1. **`git add`**: Adicione as alterações que você deseja incluir no próximo commit à área de preparação (staging area) usando: `git add`
# 
# 2. **`git commit:`** Crie um commit com as alterações adicionadas à área de preparação usando: `git commit`
# 
#     2.1 Para salvar e fechar um arquivo no Vim, você deve seguir os seguintes passos:
# 
#     2.1.1 **Salvar o arquivo:** [8]
# 
#     - Se você estiver no modo de inserção (quando você pode digitar e editar o texto), primeiro pressione `Esc` para voltar ao modo normal.
# 
#     - Depois, digite `:w` e pressione `Enter`. O `:` entra no modo de comando e `w` significa "write", ou seja, salvar o arquivo.
# 
#     2.1.2 **Fechar o arquivo:** [8]
# 
#     - Após salvar, você pode fechar o arquivo digitando `:q` e pressionando `Enter`. O q significa "quit", ou seja, sair.
# 
#     2.1.3 **Salvar e fechar em uma única etapa:** [8]
# 
#     - Se desejar fazer ambos em uma única etapa, digite `:wq` e pressione `Enter`.
# 
# Lembre-se de que se o arquivo foi aberto com permissões de administrador (usando `sudo`, por exemplo), você precisará adicionar um `!` após o comando para forçar a ação, como em `:w!` ou `:wq!`.
# 
# - **OBSERVAÇÂO(ÔES):**
# 
#     - Para editar um `commit` no `Git` que ainda não foi enviado com `git push`, você pode usar o comando: `git commit --amend`
#     
#         Esse comando permite que você modifique o último `commit` feito. Aqui está como você pode proceder:
# 
# 3. **`git push`:** Somente após concluir essas etapas, você estará pronto para fazer `git push` e enviar as alterações ao repositório remoto, usando o comando: `git push`
# 
# O comando `git push` é fundamental para colaboração em projetos de desenvolvimento em equipe, pois permite que todos os membros compartilhem suas alterações e mantenham o repositório remoto atualizado com o trabalho realizado em seus repositórios locais.

# ### 4.4 Comando `git merge` [4]
# 
# O comando `git merge` é usado para incorporar as alterações de uma ramificação (`branch`) em outra. Geralmente, você mescla uma ramificação secundária em uma ramificação principal para trazer as alterações feitas na ramificação secundária para a principal. Aqui está uma explicação mais detalhada do que o comando "git merge" faz: `git merge <nome_da_ramificação>`
# 
# 1. **<nome_da_ramificação>:** Este é o nome da ramificação que você deseja mesclar na ramificação atual (geralmente a ramificação onde você está atualmente).
# O processo de mesclagem funciona da seguinte maneira:
# 
# 2. **Escolhendo a Ramificação de Destino:** Você primeiro muda para a ramificação de destino onde deseja incorporar as alterações. Isso pode ser feito usando o comando `git checkout`, da seguinte maneira: git checkout <ramificação_destino>
# 
# 3. **Executando o `git merge`:** Após estar na ramificação de destino, você executa o comando "git merge" seguido do nome da ramificação que deseja mesclar nela. `git merge <nome_da_ramificação>`
# 
#     O `Git` tenta aplicar as alterações da ramificação especificada (<nome_da_ramificação>) na ramificação de destino.
# 
# 4. **Resolvendo Conflitos (se necessário):** Se houver conflitos entre as alterações nas duas ramificações (ou seja, se ambas tiverem modificado as mesmas partes do código), você precisará resolver esses conflitos manualmente. O `Git` sinalizará os conflitos e você deve editar os arquivos para escolher quais alterações manter.
# 
# 5. **Confirmação da Mesclagem:** Após resolver todos os conflitos (se houver), você deve confirmar a mesclagem criando um novo commit de mesclagem. O `Git` adiciona automaticamente uma mensagem de commit que descreve a mesclagem.
# 
# 6. **Finalização da Mesclagem:** Após criar o commit de mesclagem, as alterações da ramificação secundária agora estão incorporadas na ramificação de destino. Você pode continuar trabalhando na ramificação de destino ou realizar outras operações conforme necessário.
# 
# O comando `git merge` é uma ferramenta poderosa para integrar o trabalho de várias pessoas em um projeto e garantir que as alterações sejam incorporadas de maneira ordenada e controlada. Ele é frequentemente usado em fluxos de trabalho de desenvolvimento colaborativo com várias ramificações.

# ### 4.4 Comando `git stash` [9]
# 
# O comando `git stash` é usado para temporariamente salvar (ou "guardar") as mudanças em seu diretório de trabalho que ainda não foram commitadas em um estado chamado de `stash`. Isso pode ser útil quando você está trabalhando em uma determinada ramificação, mas precisa alternar para outra ramificação ou realizar alguma outra tarefa que exija um diretório de trabalho limpo.
# 
# 1. **Aqui está uma explicação do comando `git stash` em código e comentários:** Guardar as mudanças não commitadas em um `stash` com o comando: `git stash`
# 
#     Quando você executa `git stash`, o `Git` cria uma entrada de `stash` que contém todas as mudanças não commitadas em seu diretório de trabalho, incluindo os arquivos modificados e arquivos não rastreados. Seu diretório de trabalho ficará limpo, como se você nunca tivesse feito alterações. Isso permite que você faça outras tarefas, como alternar para outra ramificação, sem se preocupar com as mudanças em andamento.
# 
#     Após realizar a tarefa necessária em outra ramificação ou contexto, você pode aplicar as mudanças do stash de volta ao seu diretório de trabalho usando o comando `git stash apply` ou `git stash pop`. 
#     
#     Aqui está como fazer isso:
# 
#     - Aplica as mudanças do `stash` de volta ao diretório de trabalho: `git stash apply` ou Aplica as mudanças do `stash` de volta ao diretório de trabalho e remove o `stash`: `git stash pop`
# 
# Lembre-se de que o `stash` não substitui os `commits`. Ele é apenas uma maneira de armazenar temporariamente as mudanças em seu diretório de trabalho sem fazer um `commit`. Portanto, você pode usá-lo para alternar rapidamente entre tarefas e continuar trabalhando em suas mudanças inacabadas quando estiver pronto.

# #### 4.4.1 Comando `git stash apply stash@{0}` [9]
# 
# Para retornar as mudanças ao seu primeiro `stash`, você pode usar o comando `git stash apply` especificando qual entrada de stash deseja aplicar. As entradas de `stash` são numeradas e você pode referenciá-las pelo número. O primeiro `stash` é referenciado como `stash@{0}`. Aqui está como fazer isso:
# 
# - Aplica as mudanças do primeiro `stash` de volta ao diretório de trabalho: `git stash apply stash@{0}`
# 
#     Isso irá aplicar as mudanças do primeiro `stash` de volta ao seu diretório de trabalho, mas as mudanças ainda permanecerão no `stash`. Se você deseja remover o primeiro `stash` após aplicá-lo, você pode usar o comando `git stash drop`:
# 
# - Remove o primeiro `stash` após aplicá-lo: `git stash drop stash@{0}`
# 
# Lembre-se de que, se você tiver mais de um `stash` e quiser aplicar um `stash` específico, basta substituir `stash@{0}` pelo número da entrada de `stash` que deseja aplicar. Por exemplo, `stash@{1}` para o segundo `stash`, `stash@{2}` para o terceiro `stash`, e assim por diante.
# 
# #### 4.4.2 Comando `git restore --staged <arquivo1> <arquivo2>`
# 
# Esse comando é usado para remover arquivos ou alterações do índice (também conhecido como área de `stage`) sem modificar o seu diretório de trabalho. Ele pode ser útil quando você adicionou arquivos ao índice, mas deseja removê-los antes de efetuar um `commit`.
# 
# Aqui está como você pode usar o `git restore --staged`:
# 
# 1. Remove arquivos ou alterações do índice (`stage`): `git restore --staged <arquivo1> <arquivo2> ...`
# 
# Você pode especificar os nomes dos arquivos que deseja remover do índice como argumentos para o comando `git restore --staged`. Depois de executar esse comando, as alterações nesses arquivos serão retiradas do índice, mas as mudanças no seu diretório de trabalho permanecerão intactas. Isso significa que você pode modificar esses arquivos novamente e eles não estarão prontos para serem commitados até que você os adicione novamente ao índice usando `git add`.
# 
# Lembre-se de que o `git restore --staged` apenas remove arquivos ou alterações do índice, não descarta as mudanças do seu diretório de trabalho. Se você deseja descartar completamente as mudanças de um arquivo (tanto do índice quanto do diretório de trabalho), você pode usar `git restore --staged` seguido de `git restore` (ou `git checkout --`) como este:
# 
# 1. Remove arquivos ou alterações do índice e do diretório de trabalho
# 
#     ```
#     git restore --staged <arquivo1> <arquivo2> ...
#     git restore <arquivo1> <arquivo2> ...
#     ```
# 
# Isso descartará completamente as alterações nos arquivos especificados.
# 

# ## 6. Atualizar o repositório local (mais atualizado) para o remoto (menos atualizado) a partir que um _backup_ em outra pasta
# 
# Para atualizar o repositório local (mais atualizado) para o remoto (menos atualizado) a partir que um backup em outra pasta execute os passos abaixo:
# 
# 1. **Atribuir a palavra "Attentus" a uma variável:** `projeto="attentus_vba"`
# 
# 2. **Remover o diretório do projeto existente, se houver:** `rm -rf "$projeto"`
# 
# 3. **Clonar o repositório do `GitHub`:** `git clone git@github.com:edendenis/"$projeto"`
# 
#     3.1 Digite a senha do `GitHub` caso seja solicitado
# 
# 4. **Entrar no diretório do projeto:** `cd "$projeto"`
# 
# 5. **Remover o diretório `.git` existente, se houver:** `rm -rf .git`
# 
# 6. **Inicializar um novo repositório Git (se necessário):** `git init`
# 
# 7. **Verificar Repositórios Remotos Configurados:** Primeiro, verifique os repositórios remotos atualmente configurados no seu projeto com o comando: `git remote -v`
# 
#     7.1 **Adicionar o Repositório Remoto origin, se Necessário:** Se o origin não estiver listado, você precisará adicioná-lo. Para projetos hospedados no `GitHub` e que você deseja acessar via SSH (como indicado pela sua tentativa de usar a URL SSH `git@github.com:edendenis/[projeto].git`), use o seguinte comando: `git remote add origin git@github.com:edendenis/"$projeto".git`
# 
# 8. **Verificar a configuração do repositório remoto:** `git remote -v`
# 
# 8. **Definir o URL do repositório remoto:** `git remote set-url origin git@github.com:edendenis/"$projeto".git`
# 
# 10. **Verificar a configuração do repositório remoto:** `git remote -v`
# 
# 11. **Copiar os arquivos de backup para o diretório do projeto:** `cp -r /home/edenedfsls/Documents/EDF/APPS/excel_vba/excel_vba_public/0_BACKUP/"$projeto"/ /home/edenedfsls/Documents/EDF/APPS/excel_vba/excel_vba_public/"$projeto"/`
# 
# 10. **Verificar o status do repositório Git:** `git status`
# 
# 11. **Adicionar todos os arquivos ao staging area:** `git add .`
# 
# 12. **Remover os `arquivos/diretórios` do diretório `.references/` do staging area (se necessário):** `git rm --cached -r .references/`
# 
# 13. **Verificar o `status` do repositório Git após a remoção dos `arquivos/diretórios` do diretório `.references/`:** `git status`
# 
# 14. **Fazer `commit` das alterações:** `git commit -m "Update repository"`
# 
# 15. **Verificar o status do repositório Git após o `commit`:** `git status`
# 
# 16. **Fazer `push` das alterações e definir a ramificação local para rastrear a ramificação remota:** `git push origin HEAD:master  # git push --set-upstream origin master`
# 
#     16.1 Digite a senha do `GitHub` caso seja solicitado
# 
# 17. **Voltar para o diretório de backup:** `cd ..`
# 
# 18. **Entrar no diretório de backup:** `cd 0_BACKUP/`
# 
# 19. **Remover o diretório do projeto no backup:** `rm -rf "$projeto"`
# 
# 20. **Voltar para o diretório pai:** `cd ..`

# <!-- LICENÇA -->
# ## Licença
# 
# Distribuído sob a licença MIT. Consulte `LICENSE.txt` para obter mais informações.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- ROTEIRO -->
# ## Roteiro
# 
# - [x] Adicionar registro de alterações
# - [x] Adicionar links de volta ao topo
# - [x] Adicionar modelos adicionais com exemplos
# - [x] Suporte multilíngue
#      - [ ] Espanhol
#      - [ ] Inglês
#      - [ ] Português
#      - [x] Português brasileiro 
# 
# Consulte os [problemas abertos](https://github.com/edendenis/google_chrome/issues) para obter uma lista completa dos recursos propostos (e problemas conhecidos).
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- CONTRIBUIÇÔES -->
# ## Contribuições
# 
# As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.
# 
# Se você tiver uma sugestão que possa melhorar isso, bifurque o repositório e crie uma solicitação `pull`. Você também pode simplesmente abrir um problema com a tag “aprimoramento”.
# Não se esqueça de dar uma estrela ao projeto! Obrigado novamente!
# 
# 1. Bifurque o projeto
# 2. Crie sua ramificação de recursos (`git checkout -b feature/AmazingFeature`)
# 3. Confirme suas alterações (`git commit -m 'Add some AmazingFeature'`)
# 4. Envie para a filial (`git push origin feature/AmazingFeature`)
# 5. Abra uma solicitação pull
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- ACKNOWLEDGMENTS -->
# ## Agradecimentos
# 
# * [Best README Template](https://github.com/othneildrew/Best-README-Template?tab=readme-ov-file)
# * [Choose an Open Source License](https://choosealicense.com)
# * [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
# * [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
# * [Malven's Grid Cheatsheet](https://grid.malven.co/)
# * [Img Shields](https://shields.io)
# * [GitHub Pages](https://pages.github.com)
# * [Font Awesome](https://fontawesome.com)
# * [React Icons](https://react-icons.github.io/react-icons/search)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Referências
# 
# [1] CHACON, S e STRAUB, B.. ***Progit: everything you need to know about git***. Apress, Second edition, 2020.
# 
# [2] OPEN AI. ***Enviar repositório local ao GitHub.*** Disponível em: <https://chat.openai.com/c/0b137275-7e88-41e4-b679-6ebce8603a01> (texto adaptado). ChatGPT. Acessado em: 03/08/2023 09:09.
# 
# [3] CHACON, S e STRAUB, B.. ***Progit: everything you need to know about git***. Apress, page 16, Second edition, 2020.
# 
# [4] OPEN AI. ***GitLab: comando "git fetch".*** Disponível em: <https://chat.openai.com/c/31c7e7f1-51c8-47ae-978b-6a01c5730131> (texto adaptado). ChatGPT. Acesso em: 20/09/2023 21:38.
# 
# [5] OPEN AI. ***Gerar chave SSH Ubuntu.*** Disponível em: <https://chat.openai.com/c/6f3224a3-b4a2-43c6-a878-f1612beae966> (texto adaptado). Chat GPT. Acessado em: 21/07/2023 10:14.
# 
# [6] OPEN AI. ***Gerar chave SSH Ubuntu.*** Disponível em: <https://chat.openai.com/c/3d4690a0-2466-4655-990a-cd14823b6825> (texto adaptado). Chat GPT. Acessado em: 21/07/2023 10:21.
# 
# [7] OPEN AI. ***Comando "git log --oneline".*** Disponível em: <https://chat.openai.com/c/7c186067-7c88-4f26-bdd0-3ac8d9036ffd> (texto adaptado). Chat GPT. Acessado em: 09/11/2023 10:24.
# 
# [8] OPEN AI. ***Salvar e fechar no vim.*** Disponível em: <https://chat.openai.com/c/efd5cbbb-2acb-4d58-8a04-9887d73fb8e8> (texto adaptado). Chat GPT. Acessado em: 09/11/2023 15:37.
# 
# [9] OPEN AI. ***Remover arquivos da staging.*** Disponível em: <https://chat.openai.com/c/d640a993-7f4d-41c4-923e-3ccc5d04f709> (texto adaptado). Chat GPT. Acessado em: 22/11/2023 12:04.
# 
