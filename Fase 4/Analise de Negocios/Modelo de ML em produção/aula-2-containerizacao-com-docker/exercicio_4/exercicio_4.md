# Exercício 4 

Vamos criar um projeto simples que utiliza dois scripts Python (`app_1.py` e `app_2.py`) e um `docker-compose.yml` para orquestrar a execução de ambos. Primeiro, vamos criar a seguinte estrutura de diretórios: 

```bash 
exercicio_4/ 
​​├── app1/​ 
​​│   └── app_1.py​ 
​​├── app2/​ 
​​│   └── app_2.py​ 
​​└── docker-compose.yml​ 
``` 

1. Crie o `app_1.py` 

No diretório `app1/`, crie o arquivo `app_1.py` com o seguinte conteúdo: 

```python 
print("Hello world!") 
``` 

2. Crie o `app_2.py` 

No diretório app2/, crie o arquivo app_2.py com o seguinte conteúdo: 

```python 
print("Hello world again!") 
``` 

3. Crie o `docker-compose.yml`

Na raiz do diretório `exercicio_4/`, crie o arquivo `docker-compose.yml` com o seguinte conteúdo: 

```yaml 
version: "3.9" 

services: 
  app1: 
    image: python:3.9-slim 
    volumes: 
      - ./app_1:/app 
    working_dir: /app
    command: "python app_1.py" 
  app2: 
    image: python:3.9-slim 
    volumes: 
      - ./app_2:/app 
    working_dir: /app 
    command: "python app_2.py" 
``` 

4. Inicie a aplicação com Docker Compose 

Na raiz do diretório `exercicio_4/`, execute o comando: 

```bash 
docker-compose up 
``` 

O Docker Compose irá baixar as imagens e executar os containers. Os outputs serão exibidos no seu terminal. 

5. Verifique os logs 

Verifique as saídas no seu terminal para ver os logs gerados por cada aplicação. Você deve ver "Hello world!" sendo impresso a partir de um container e "Hello world again!" sendo impresso a partir do outro. 

6. Pare a aplicação 

Na raiz do diretório `exercicio_4/`, execute o comando: 

```bash 
docker-compose down 
``` 

O Docker Compose irá remover todos os containers criados para a aplicação. 

Este exercício demonstrou como o Docker Compose facilita a execução de múltiplas aplicações simultaneamente, permitindo a criação de ambientes complexos de forma simples e organizada. E como vimos, o arquivo `docker-compose.yml` torna o processo de deploy mais gerenciável. 