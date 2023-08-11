#Importação das bibliotecas
import streamlit as st 
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import DropFeatures, OneHotEncodingNames, OrdinalFeature, MinMaxWithFeatNames
from sklearn.pipeline import Pipeline
import joblib
from joblib import load

#carregando os dados 
dados = pd.read_csv('https://raw.githubusercontent.com/alura-tech/alura-tech-pos-data-science-credit-scoring-streamlit/main/df_clean.csv')


############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Formulário para Solicitação de Cartão de Crédito 🤑</h1>", unsafe_allow_html = True)

st.warning('Preencha o formulário com todos os seus dados pessoais e clique no botão **ENVIAR** no final da página.')

# Idade
st.write('### Idade')
input_idade = float(st.slider('Selecione a sua idade', 18, 100))

# Grau de escolaridade
st.write('### Nível de escolaridade')
input_grau_escolaridade = st.selectbox('Qual o Grau de Escolaridade ?', dados['Grau_escolaridade'].unique())

# Estado civil
st.write('### Estado civil')
input_estado_civil = st.selectbox('Qual é o seu estado civil ?', dados['Estado_civil'].unique())

# Número de membros da família
st.write('### Família')
membros_familia = float(st.slider('Selecione quantos membros tem na sua família', 1, 20))

# Carro próprio
st.write('### Carro próprio')
input_carro_proprio = st.radio('Você possui um automóvel?',['Sim','Não'], index=0)
input_carro_proprio_dict = {'Sim': 1, 'Não':0}
input_carro_proprio = input_carro_proprio_dict.get(input_carro_proprio)

# Casa própria
st.write('### Casa própria')
input_casa_propria = st.radio('Você possui uma propriedade?',['Sim','Não'], index=0)
input_casa_propria_dict = {'Sim': 1, 'Não':0}
input_casa_propria = input_casa_propria_dict.get(input_casa_propria)

# Moradia
st.write('### Tipo de residência')
input_tipo_moradia = st.selectbox('Qual é o seu tipo de moradia ?', dados['Moradia'].unique())

# Situação de emprego
st.write('### Categoria de renda')
input_categoria_renda = st.selectbox('Qual é a sua categoria de renda ?', dados['Categoria_de_renda'].unique())

# Ocupação
st.write('### Ocupação')
input_ocupacao = st.selectbox('Qual é a sua ocupação ?', dados['Ocupacao'].unique())

# Tempo de experiência
st.write('### Experiência')
input_tempo_experiencia = float(st.slider('Selecione o seu tempo de experiência em anos', 0,30))

# Rendimentos
st.write('### Rendimentos')
input_rendimentos = float(st.text_input('Digite o seu rendimento anual (em reais) e pressione ENTER para confirmar',0))

# Telefone trabalho
st.write('### Telefone corporativo')
input_telefone_trabalho = st.radio('Você tem um telefone corporativo?',['Sim','Não'], index=0)
telefone_trabalho_dict = {'Sim': 1, 'Não':0}
telefone_trabalho = telefone_trabalho_dict.get(input_telefone_trabalho)

# Telefone fixo
st.write('### Telefone fixo')
input_telefone = st.radio('Você tem um telefone fixo?',['Sim','Não'], index=0)
telefone_dict = {'Sim': 1, 'Não':0}
telefone = telefone_dict.get(input_telefone)

# Email 
st.write('### Email')
input_email = st.radio('Você tem um email?',['Sim','Não'], index=0)
email_dict = {'Sim': 1, 'Não':0}
email = email_dict.get(input_email)

# Lista de todas as variáveis: 
novo_cliente = [0, # ID_Cliente
                    input_carro_proprio, # Tem_carro
                    input_casa_propria, # Tem_Casa_Propria
                    telefone_trabalho, # Tem_telefone_trabalho
                    telefone, # Tem_telefone_fixo
                    email,  # Tem_email
                    membros_familia,  # Tamanho_Familia
                    input_rendimentos, # Rendimento_anual	
                    input_idade, # Idade
                    input_tempo_experiencia, # Anos_empregado
                    input_categoria_renda, # Categoria_de_renda
                    input_grau_escolaridade, # Grau_Escolaridade
                    input_estado_civil, # Estado_Civil	
                    input_tipo_moradia, # Moradia                                                  
                    input_ocupacao, # Ocupacao
                     0 # target (Mau)
                    ]


# Separando os dados em treino e teste
def data_split(df, test_size):
    SEED = 1561651
    treino_df, teste_df = train_test_split(df, test_size=test_size, random_state=SEED)
    return treino_df.reset_index(drop=True), teste_df.reset_index(drop=True)

treino_df, teste_df = data_split(dados, 0.2)

#Criando novo cliente
cliente_predict_df = pd.DataFrame([novo_cliente],columns=teste_df.columns)

#Concatenando novo cliente ao dataframe dos dados de teste
teste_novo_cliente  = pd.concat([teste_df,cliente_predict_df],ignore_index=True)

#Pipeline
def pipeline_teste(df):

    pipeline = Pipeline([
        ('feature_dropper', DropFeatures()),
        ('OneHotEncoding', OneHotEncodingNames()),
        ('ordinal_feature', OrdinalFeature()),
        ('min_max_scaler', MinMaxWithFeatNames()),
    ])
    df_pipeline = pipeline.fit_transform(df)
    return df_pipeline

#Aplicando a pipeline
teste_novo_cliente = pipeline_teste(teste_novo_cliente)

#retirando a coluna target
cliente_pred = teste_novo_cliente.drop(['Mau'], axis=1)

#Predições 
if st.button('Enviar'):
    model = joblib.load('modelo/xgb.joblib')
    final_pred = model.predict(cliente_pred)
    if final_pred[-1] == 0:
        st.success('### Parabéns! Você teve o cartão de crédito aprovado')
        st.balloons()
    else:
        st.error('### Infelizmente, não podemos liberar crédito para você agora!')
 
