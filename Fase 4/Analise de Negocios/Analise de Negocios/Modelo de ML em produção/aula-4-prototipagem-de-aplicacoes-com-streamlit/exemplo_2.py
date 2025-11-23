import streamlit as st
import pandas as pd

# Gerando dados fictícios
data = {
    "Nome": ["Alice", "Bob", "Carlos"],
    "Idade": [24, 30, 29],
    "Profissão": ["Engenheira", "Médico", "Professor"]
}

df = pd.DataFrame(data)

# Exibindo os dados em tabela
st.title("Tabela de Dados")
st.write("Aqui está uma tabela gerada com Pandas:")
st.dataframe(df)
