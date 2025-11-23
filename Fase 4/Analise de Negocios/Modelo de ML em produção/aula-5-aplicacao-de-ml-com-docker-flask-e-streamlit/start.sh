#!/bin/bash

echo "Treinando o modelo..."
docker-compose run trainer

echo "Iniciando a API..."
docker-compose up -d api

echo "Verificando API..."
until curl -s http://localhost:5000/ > /dev/null; do
    echo "Aguardando API..."
    sleep 2
done

echo "Iniciando Streamlit..."
docker-compose up -d streamlit
