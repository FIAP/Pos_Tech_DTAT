import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Carregando dados e modelo
iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

# Interface para predição
st.title("Classificador de Flores Iris")
st.write("Preencha as características da flor:")

sepal_length = st.slider("Comprimento da Sépala", 4.0, 8.0, 5.0)
sepal_width = st.slider("Largura da Sépala", 2.0, 4.5, 3.0)
petal_length = st.slider("Comprimento da Pétala", 1.0, 7.0, 4.0)
petal_width = st.slider("Largura da Pétala", 0.1, 2.5, 1.0)

# Predição
pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
classe = iris.target_names[pred[0]]

st.write(f"A flor provavelmente é da classe: {classe}")
