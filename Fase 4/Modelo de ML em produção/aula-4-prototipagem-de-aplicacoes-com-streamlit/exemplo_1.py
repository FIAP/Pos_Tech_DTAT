import streamlit as st

# Título e cabeçalho
st.title("Bem-vindo ao Streamlit!")
st.header("Este é um protótipo simples")

# Texto básico
st.write("Streamlit é uma biblioteca Python para criar aplicações web interativas.")

# Botões interativos
if st.button("Clique aqui!"):
    st.write("Você clicou no botão!")

# Entrada de texto
nome = st.text_input("Digite seu nome")
if nome:
    st.write(f"Olá, {nome}!")
