# Exercício 2 

Agora vamos criar uma pasta chamada `exercicio_2` copiar e modificar o app.py para incluir uma biblioteca externa do Python (requests) e atualizar o `Dockerfile` com instruções adicionais, como RUN para instalar dependências, além de incluir `ENV`, `WORKDIR` e `EXPOSE`. 

1. Modificando o app.py 

Atualize o conteúdo do arquivo app.py para fazer uma requisição HTTP simples usando a biblioteca requests. O novo conteúdo do app.py será: 

```python 
import requests 

response = requests.get("https://api.github.com") 
print(f"Status Code: {response.status_code}") 
print(f"Response JSON: {response.json()}") 
``` 

2. Atualizando o Dockerfile 

O novo `Dockerfile` incluirá instruções para: 

- Instalar o requests via `pip`; 

- Definir uma variável de ambiente (`ENV`); 

- Configurar um diretório de trabalho (`WORKDIR`); 

Expor uma porta (`EXPOSE`), caso a aplicação seja uma API ou serviço. 

Segue o novo conteúdo do Dockerfile: 

```Dockerfile 
# imagem base do Python 
FROM python:3.9-slim 

# configura uma variável de ambiente 
ENV PYTHONUNBUFFERED=1 

# define o diretório de trabalho no container 
WORKDIR /app 

# copia o arquivo de script Python para o container 
COPY app.py /app/app.py 

# instala a biblioteca requests 
RUN pip install requests 

# expõe a porta 80 (caso a aplicação seja uma API, por exemplo) 
EXPOSE 80 

# define o comando para rodar o script quando o container for executado 
CMD ["python", "app.py"] 
``` 

Explicação das instruções adicionadas no `Dockerfile`: 

- **`ENV PYTHONUNBUFFERED=1`**: Define uma variável de ambiente para evitar o buffer na saída do Python, garantindo que os logs apareçam em tempo real; 

- **`WORKDIR /app`**: Configura o diretório de trabalho dentro do container. Isso significa que todos os comandos subsequentes no Dockerfile serão executados a partir de /app; 

- **`RUN pip install requests`**: Instala a biblioteca `requests` no container. 

- **`EXPOSE 80`**: Informa que a aplicação está configurada para escutar na porta 80. Embora não seja necessário para a execução do script atual, essa instrução pode ser útil para APIs ou serviços web. 

3. Construindo a imagem 

Para construir a imagem Docker com o nome `hello-requests`, execute o seguinte comando no terminal: 

```bash 
docker build -t hello-requests . 
``` 

4. Executando o container 

Agora, execute o container para ver a saída do script: 

```bash 
docker run hello-requests 
``` 

É esperado que seja imprimido o status e a resposta da requisição HTTP feita para a API do GitHub.