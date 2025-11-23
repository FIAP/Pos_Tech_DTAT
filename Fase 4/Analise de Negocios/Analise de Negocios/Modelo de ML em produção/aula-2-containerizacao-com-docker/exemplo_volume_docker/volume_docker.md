# Volume no Docker

Aqui veremos um exemplo de persistência de dados no volume do Docker. 

Para criar um volume nomeado, executar: 

```bash 
docker volume create dados_app 
``` 

Agora executamos um container usando este volume e criamos um arquivo no volume: 

```bash 
docker run -d --name app_volumes -v dados_app:/app python:3.9-slim \ 

bash -c 'echo "Hello, Docker!" >> /app/mensagem.txt' 
``` 

Agora podemos verificar se o arquivo foi persistido no volume. Vamos parar e remover o container. 

```bash 
docker stop app_volumes 
```

E depois:

```bash
docker rm app_volumes 
``` 

Vamos recriar o container usando o mesmo volume. 

```bash 
docker run -it --name app_volumes -v dados_app:/app python:3.9-slim bash 
``` 

E ao acessar o container, é esperado que o arquivo mensagem.txt esteja no volume. 

```bash 
cat /app/mensagem.txt 
``` 

Se o seguinte conteúdo do arquivo for exibido, o volume está funcionando corretamente e o dado foi persistido. 

``` 
Hello, Docker! 
``` 