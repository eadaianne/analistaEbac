# Linux

Módulo com foco em Linux. Os principais temas abordados:
* Comandos básicos
* Controle de usuários e permissões
* Shell script

> Tecnicamente, Linux não é um sistema operacional, é um kernel (componente central de um SO). Ele não possui interface gráfica, e há varios SO's que usam esse kernel (Ubuntu, Red Hat, Mint, etc).

> **Filosofia open-source**: código aberto e desenvolvido de forma colaborativa, teoricamente qualquer um pode desenvolver um SO utilizando o kernel Linux.

---

## WSL
Subsistema do Windows para Linux, permite instalar e executar distribuições Linux no Windows (integração dos SO).

**Instruções de instalação:** https://learn.microsoft.com/pt-br/windows/wsl/install

> wsl --list --online\
> wsl --install --distribution '[nome da distribuição]'\
> **OBS:** instalar rodando power shell como administrador.

---
## Primeiros comandos Linux
> Comandos no terminal de Ubuntu.

> [comando] --help - explicação sobre o comando

1. pwd - mostra o diretório atual
2. ls - lista os dirretórios dentro do diretório atual
    1. ls /[nome] - lista diretórios em [nome]
    2. ls / - lista a raiz do sistema
    3. ls /etc - lista arquivos de configuração
    4. ls -R /[nome] - lista de forma recursiva
3. cd [nome] - vai para o diretório [nome]
4. mkdir [/nome] - cria diretórios
    1. mkdir -p [nome/nome2] - cria estrutura de diretórios
5. rmdir - apaga diretórios, mas apenas em branco
6. touch [dir/nome] - cria um arquivo vazio
7. du -h [nomedir] - mostra o tamanho do diretório
    1. du -sh - idem, mas resume
8. df -h - mostra tamanho dos sistemas


### Editores de texto
1. nano [nome arquivo]
    1. nano -l [nome] - número de linhas
2. vim [nome]

### Manipulação de arquivos
1. cp [nome] [destino] - copia arquivo [nome]
    1. adicionar outro nome no caminho do destino altera o nome da cópia
2. mv [nome] [destino] - move arquivo [nome]
3. rm [nome] - remove arquivo [nome]
4. head [nome] - mostra inicio do documento
5. tail [nome] - mostra fim do documento
6. cat - versátil, pode criar, editar ou visualizar arquivos. Pesquisar especificidades depois.

