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

dt_hoje_str = ?

caminho_input= '/home/airflow/Documents/airflowFIAP/codigos/tickers.csv'
caminho_output= os.path.join(?, ?) 

df_acoes = pd.read_csv(caminho_input)

#print(df_acoes.count())

if not os.path.exists(?):
    os.makedirs(?)

end_date = ?
start_date = ?

for ?:
    ?