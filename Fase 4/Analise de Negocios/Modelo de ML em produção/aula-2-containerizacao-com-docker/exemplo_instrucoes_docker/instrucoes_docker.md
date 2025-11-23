# Instruções Docker

Instruções Docker são usadas nos **`Dockerfiles`** para construir imagens.

## Formato de um Dockerfile 

O Dockerfile contém instruções que começam com um comentário, seguidas pela instrução em letras maiusculas e seu argumento em minúsculas. A ordem das instruções é importante e define a sequência de **build** do container. 

As principais instruções do Docker são: 

**`FROM`**: Define a imagem base a ser usada; 

**`COPY`**: Copia arquivos ou pastas para o container; 

**`RUN`**: Executa comandos dentro do container; 

**`CMD`**: Especifica o comando padrão que será executado quando o container iniciar. 

As instruções são montadas começando pela **`FROM`**, seguida de **`COPY`**, **`RUN`**, e finalizando com **`CMD`**.

Exemplo: 

```Dockerfile
# usa a imagem base do Python slim
FROM python:3.9-slim

# define o diretório de trabalho dentro do container
WORKDIR /app

# copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# instala as dependências do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copia o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# define o comando padrão que será executado quando o container iniciar
CMD ["python", "app.py"]
```

Explicação do **`Dockerfile`**:

- **`FROM python:3.9-slim`**: Define a imagem base como `python:3.9-slim`, que é uma versão leve do Python 3.9.

- **`WORKDIR /app`**: Define o diretório de trabalho dentro do container como `/app`. Todos os comandos subsequentes serão executados neste diretório.

- **`COPY requirements.txt .`**: Copia o arquivo `requirements.txt` do host para o diretório de trabalho no container.

- **`RUN pip install --no-cache-dir -r requirements.txt`**: Executa o comando para instalar as dependências listadas no `requirements.txt`. A opção `--no-cache-dir` é usada para evitar o armazenamento em cache dos pacotes instalados, reduzindo o tamanho da imagem final.

- **`COPY . .`**: Copia todos os arquivos do diretório atual do host para o diretório de trabalho no container.

- **`CMD ["python", "app.py"]`**: Define o comando padrão que será executado quando o container iniciar. Neste caso, ele executa o script `app.py` usando o interpretador Python.
