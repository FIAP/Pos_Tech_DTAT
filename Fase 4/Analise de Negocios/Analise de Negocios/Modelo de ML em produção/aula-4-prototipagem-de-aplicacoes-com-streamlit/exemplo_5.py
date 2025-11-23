import streamlit as st
import pandas as pd

# Carregando o arquivo CSV
st.title("Carregue seu Arquivo CSV")
uploaded_file = st.file_uploader("Escolha o arquivo", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dados do arquivo carregado:")
    st.dataframe(df)
