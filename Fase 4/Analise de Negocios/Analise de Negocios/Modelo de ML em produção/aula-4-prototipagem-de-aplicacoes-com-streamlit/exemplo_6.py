import streamlit as st
import pandas as pd

# Dados fictícios
data = {
    "Produto": ["A", "B", "C", "D"],
    "Vendas": [100, 200, 150, 300],
    "Região": ["Norte", "Sul", "Leste", "Oeste"]
}
df = pd.DataFrame(data)

# Filtro
regiao = st.selectbox("Selecione a Região", df["Região"].unique())

# Filtrando dados
dados_filtrados = df[df["Região"] == regiao]

# Exibindo tabela e resumo
st.title("Dashboard de Vendas")
st.subheader(f"Dados da Região: {regiao}")
st.dataframe(dados_filtrados)

st.write("Total de Vendas:")
st.write(dados_filtrados["Vendas"].sum())
