# Primeiros comandos Linux
> Comandos no terminal de Ubuntu.

> [comando] --help - explicação sobre o comando

1. pwd - mostra o diretório atual
2. ls - lista os dirretórios dentro do diretório atual
    1. ls /[nome] - lista diretórios em [nome]
    2. ls / - lista a raiz do sistema
    3. ls /etc - lista arquivos de configuração
    4. ls -R /[nome] - lista de forma recursiva
    5. ls -l -mais informações
3. cd [nome] - vai para o diretório [nome]
4. mkdir [/nome] - cria diretórios
    1. mkdir -p [nome/nome2] - cria estrutura de diretórios
5. rmdir - apaga diretórios, mas apenas em branco
6. touch [dir/nome] - cria um arquivo vazio
7. du -h [nomedir] - mostra o tamanho do diretório
    1. du -sh - idem, mas resume
8. df -h - mostra tamanho dos sistemas


## Editores de texto
1. nano [nome arquivo]
    1. nano -l [nome] - número de linhas
2. vim [nome]

## Manipulação de arquivos
1. cp [nome] [destino] - copia arquivo [nome]
    1. adicionar outro nome no caminho do destino altera o nome da cópia
2. mv [nome] [destino] - move arquivo [nome]
3. rm [nome] - remove arquivo [nome]
4. head [nome] - mostra inicio do documento
5. tail [nome] - mostra fim do documento
6. cat - versátil, pode criar, editar ou visualizar arquivos. Pesquisar especificidades depois.

## Controle de usuários
1. sudo (antes de um comando) - executa um comando como administrador
2. sudo su - substitui usuário root (dá todas as permissões ao user atual)
3. exit - sai da sessão
4. whoami - mostra user atual
5. who - infos de user
6. uname -a - mostra infos do SO

> Há usuários e grupos de usuários. 

7. chown [user]:[grupo] [arquivo ou diretório] - altera o dono de determinado arquivo ou diretório

> Lembrar de pesquisar mais a fundo sobre usuários, grupos de usuários e como definir permissões.

> Ao listar com ls -l, a explicação das colunas é:
> 1. 10 caracteres. O primeiro indica se é um arquivo (-) ou um diretório (d). Os outros nove são lidos de três em três e indicam respectivamente permissões do dono do arquivo, permissões do grupo do dono do arquivo e permissões dos demais. Normalmente, rwx (read, write, execute).
>2. quantidade de arquivos ou subdiretórios.
>3. dono do arquivo.
>4. grupo do dono do arquivo.
>5. tamanho em bytes dos arquivos e diretórios.
>6. mês, dia, ano e horário da última alteração.
>7. nome do arquivo.

8. chmod [opções] [arquivo] - altera permissões no arquivo

>"Opções": ugo (user, group, others) | +-= (adicionar, remover, definir) | rwx

>Exemplos: 
> * Adicionar permissão de execução no arquivo: chmod +x arquivo.txt
> * Adicionar permissão de leitura e escrita no arquivo para usuário: chmod u+rw doc.txt
> * Remover permissão de execução para grupos e outros: chmod go-w doc.txt

>Permissões por números   
> r: 4 | w: 2 | x: 1 | nenhuma: 0   
> somar números pra mais de uma permissão (ex: rx = 5)   
   
> **Exemplo:** chmod 755 a.txt | **chmod [num_user num_grupo num_outros]**