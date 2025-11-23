import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Gerando o gráfico
fig, ax = plt.subplots()
ax.plot(x, y, label="Seno")
ax.set_title("Gráfico de Seno")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

# Exibindo o gráfico
st.title("Visualizando Gráficos")
st.pyplot(fig)
