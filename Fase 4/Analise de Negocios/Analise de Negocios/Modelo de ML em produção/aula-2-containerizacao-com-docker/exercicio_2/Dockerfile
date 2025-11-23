# Use a imagem base do Python
FROM python:3.9-slim

# Configura uma variável de ambiente
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de script Python para o container
COPY app.py /app/app.py

# Instala a biblioteca requests
RUN pip install requests

# Expõe a porta 80 (caso a aplicação seja uma API, por exemplo)
EXPOSE 80

# Define o comando para rodar o script quando o container for executado
CMD ["python", "app.py"]
