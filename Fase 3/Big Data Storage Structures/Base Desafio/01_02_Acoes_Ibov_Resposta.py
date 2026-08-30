#### Nota do Desenvolvedor ####
#       Nome: Vinicius Henrique dos Santos
#       Objetivo: Criar um script que faca o download de informacoes de cotacao para acoes passadas como parametro pelos usuarios
#                 - Realizar o download dos dados de bolsa de valores de acordo com o imput dos usuarios em csv
#                 - Verificar se existe e criar uma pasta na rede com a data corrente no formato AAAAMMDD para depositar um arquivo para cada ticker
#                 - Os consumidores usarao esses dados em formato csv, esse arquivo deve ser individual para cada ticker
#                 - Os dados de cotacao deverao ter informacoes dos ultimos 5 pregoes
#                 - Crie uma coluna chamada Amplitude_do_Preco, calculada pela diferenca de preco entre a maior e a menor cotacao desse ticker
#                 - Crie uma coluna chamada Total_RS_Negociado, calculada pelo volume (quantidade de acoes) multiplicada pela cotacao de fechamento

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os

dt_hoje_str = datetime.now().strftime('%Y%m%d') 

caminho_input= '/home/airflow/Documents/airflowFIAP/codigos/tickers.csv'
caminho_output= os.path.join('/home/airflow/Documents/airflowFIAP/codigos/acoes', dt_hoje_str) 

df_acoes = pd.read_csv(caminho_input)

#print(df_acoes.count())

if not os.path.exists(caminho_output):
    os.makedirs(caminho_output)

end_date = datetime.now()
start_date = end_date - timedelta(days=15)

for ticker in df_acoes['Ticker']:
    df_dados_bolsa = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

    df_dados_bolsa.index = pd.to_datetime(df_dados_bolsa.index)
    ultimo_dia_pregao = df_dados_bolsa.index.max()
    sete_dias_atras = ultimo_dia_pregao - timedelta(days=7) #7 dias pois nao temos pregoes aos finais de semana
    mascara_data = (df_dados_bolsa.index > sete_dias_atras) & (df_dados_bolsa.index <= ultimo_dia_pregao)
    
    df_ultimos_5_pregoes = df_dados_bolsa.loc[mascara_data].copy()

    #Criando duas novas variaveis para entregar prontas aos consumidores:

    df_ultimos_5_pregoes.loc[:, 'Amplitude_do_Preco'] = df_ultimos_5_pregoes['High'] - df_ultimos_5_pregoes['Low']
    df_ultimos_5_pregoes.loc[:, 'Total_RS_Negociado'] = df_ultimos_5_pregoes['Close'] * df_ultimos_5_pregoes['Volume']

    nome_arquivo = f"{ticker.replace('.SA', '')}_ultimos_5_pregoes.csv"
    df_ultimos_5_pregoes.to_csv(os.path.join(caminho_output, nome_arquivo))
    
    print(f"Dados para {ticker} salvos em {nome_arquivo}")