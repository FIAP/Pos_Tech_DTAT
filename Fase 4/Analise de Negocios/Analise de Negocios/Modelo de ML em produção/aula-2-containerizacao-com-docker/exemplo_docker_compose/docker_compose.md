# Docker compose 

O Docker Compose é uma ferramenta que permite definir e gerenciar aplicações multi-container. Ele utiliza um arquivo YAML para configurar todos os serviços, redes e volumes necessários para uma aplicação e permite que você possa subir, parar e gerenciar todos eles com um único comando. Imagine o Docker Compose como um “orquestrador” que gerencia e interliga diversos containers, facilitando o gerenciamento de aplicações complexas. 

Com Docker Compose você pode definir: 

- **Serviços**: Cada serviço corresponde a um container Docker com suas especificações (imagem, variáveis de ambiente, volumes, portas, etc); 

- **Redes**: As redes que interligam os containers, facilitando a comunicação entre eles; 

- **Volumes**: Os volumes que persistem dados entre os containers e o host. 

O Docker Compose simplifica a criação e o gerenciamento de aplicações multi-container. Ao invés de executar múltiplos comandos docker run, você define sua aplicação em um arquivo **`docker-compose.yml`** e utiliza comandos do Docker Compose para subir, gerenciar e parar toda a aplicação. Além disso, Docker Compose facilita o trabalho em equipe e a garantia de que todos os containers serão executados com as mesmas configurações, eliminando surpresas e facilitando o processo de desenvolvimento. 

O arquivo **`docker-compose.yml`** é onde você declara todos os serviços que compõem sua aplicação. Veja um exemplo de um arquivo docker-compose.yml: 

 

```yaml 
version: "3.9" 

services: 
  app1: 
    image: python:3.9-slim 
    volumes: 
      - ./app1:/app 
    command: "python /app/app_1.py" 
  app2: 
    image: python:3.9-slim 
    volumes: 
      - ./app2:/app 
    command: "python /app/app_2.py" 
``` 

Explicando o **`docker-compose.yml`** Nesse exemplo, temos: 

- **`version`**: A versão do formato do docker-compose.yml; 

**`services`**: Contém a definição de todos os serviços; 

**`app1`**: Um serviço chamado `app1` que usa a imagem `python:3.9-slim`, monta o diretório local `./app1` no diretório `/app` do container e executa o comando `python /app/app_1.py`; 

**`app2`**: Um serviço chamado `app2` que usa a imagem `python:3.9-slim`, monta o diretório local `./app2` no diretório `/app` do container e executa o comando `python /app/app_2.py`. 

## Comandos do Docker Compose 

Aqui estão alguns comandos essenciais do Docker Compose: 

**`docker-compose up`**: Cria e inicia todos os containers definidos no arquivo `docker-compose.yml`. Por padrão, ele procura o arquivo no diretório atual; 

**`docker-compose up -d`**: Executa o comando up em modo *detached*, ou seja, ele executa os containers em background, sem travar seu terminal; 

**`docker-compose down`**: Remove todos os containers, redes e volumes criados pelo docker-compose; 

**`docker-compose stop`**: Para todos os containers, mas os mantêm no sistema; 

**`docker-compose start`**: Inicia os containers parados; 

**`docker-compose logs`**: Visualiza os logs dos containers. 