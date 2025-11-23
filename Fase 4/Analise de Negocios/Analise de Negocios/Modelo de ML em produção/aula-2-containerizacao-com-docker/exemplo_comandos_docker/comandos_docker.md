# Comandos do Docker

Dado que temos o **`Dockerfile`**, podemos executar comandos Docker no terminal para criação de imagens e containers. Os principais comandos Docker são: 

**`docker build`**: Cria uma imagem a partir de um Dockerfile. 

**`docker run`**: Cria e executa um container a partir de uma imagem Docker. 

Para explorar mais comandos Docker e entender o gerenciamento de containers e imagens, vamos abordar os principais comandos para operações cotidianas. 

Comandos básicos para gerenciamento de imagens e containers: 

**`docker ps`**: Lista os containers em execução no momento, ou seja apenas containers ativos; 

**`docker ps -a`**: Para listar todos os containers, incluindo os que estão parados; 

**`docker rm`**: Remove um ou mais containers parados, para remover múltiplos containers, forneça os IDs ou nomes separados por espaço; 

**`docker rmi`**: Remove uma ou mais imagens Docker. para remover uma imagem, forneça o ID ou nome da imagem;as as imagens; 

**`docker logs`**: Exibe os logs gerados por um container em execução ou que já foi executado, esse comando pode ser útil para depurar erros ou ver a saída da aplicação; 

**`docker exec`**: Executa um comando dentro de um container em execução. Comumente usado para acessar o terminal de um container com bash ou sh. Exemplos de execução: 

```bash 

docker exec -it <container_id> bash  # abre um terminal bash interativo dentro do container 

docker exec <container_id> <command> # executa um comando específico no container 

``` 

Esses comandos são fundamentais para gerenciar imagens e containers no Docker. Eles facilitam a automação e o gerenciamento de ambientes, tornando o desenvolvimento e a operação mais eficientes. Para mais informações e casos de uso, acessar a documentação do Docker: https://docs.docker.com/manuals/