#!/usr/bin/env pwsh

Write-Output "Treinando o modelo..."
docker-compose run trainer

Write-Output "Iniciando a API..."
docker-compose up -d api

Write-Output "Verificando API..."
do {
    Write-Output "Aguardando API..."
    Start-Sleep -Seconds 2
} until (Test-NetConnection -ComputerName localhost -Port 5000 -InformationLevel Quiet)

Write-Output "Iniciando Streamlit..."
docker-compose up -d streamlit
