import streamlit as st
import plotly.express as px
import pandas as pd

# Dados para o gráfico
df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [23, 45, 56, 78]
})

# Criando gráfico de barras
fig = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Barras Interativo")

# Exibindo no Streamlit
st.title("Gráficos Interativos com Plotly")
st.plotly_chart(fig)
