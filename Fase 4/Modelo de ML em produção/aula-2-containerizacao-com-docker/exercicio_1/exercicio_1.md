## Exercício 1 

Vamos criar um container Docker que executa um script Python imprimindo "Hello world!". É necessário ter o Docker Desktop instalado em sua máquina local. 

1. Crie um arquivo Python chamado app.py em uma pasta chamada exercicio_1 com o seguinte conteúdo: 

```python 
print("Hello world!") 
``` 

2. Crie um arquivo Dockerfile no mesmo diretório com o seguinte conteúdo: 

```Dockerfile 
# imagem base do Python 
FROM python:3.9-slim 

# instrução copiar o script Python para o container 
COPY app.py /app.py 

# instrução para rodar o script quando o container Docker for executado 
CMD ["python", "/app.py"] 
``` 

3. Construa (ou “faça o build”) a imagem Docker com nome “hello-world” executando o comando no terminal: 

```bash 
docker build -t hello-world . 
``` 

É esperado que a imagem criada esteja visível no Docker Desktop.

4. Execute o container com o comando: 

```bash 
docker run hello-world 
``` 

Com isso é esperado executar um container que imprime "Hello world!"