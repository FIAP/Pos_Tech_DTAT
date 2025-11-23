import streamlit as st
import requests

st.title("Previsão de Carga de Aquecimento")
st.write("Insira os valores das variáveis preditoras com base nas características do edifício:")

# Campos de entrada com unidades de medida nas descrições
RelativeCompactness = st.number_input("Compacidade Relativa (adimensional)", value=0.75)
SurfaceArea = st.number_input("Área da Superfície (m²)", value=500.0)
WallArea = st.number_input("Área da Parede (m²)", value=300.0)
RoofArea = st.number_input("Área do Telhado (m²)", value=150.0)
OverallHeight = st.number_input("Altura Total (m)", value=3.0)
Orientation = st.selectbox("Orientação (2=Norte, 3=Leste, 4=Sul, 5=Oeste)", options=[2, 3, 4, 5])
GlazingArea = st.number_input("Área de Vidro (adimensional)", value=0.1)
GlazingAreaDistribution = st.selectbox("Distribuição da Área de Vidro (0=Sem, 1-4=Distribuições)", options=[0, 1, 2, 3, 4])

# Botão para realizar a predição
if st.button("Prever"):
    # Preparar os dados para envio à API
    input_data = {
        "RelativeCompactness": RelativeCompactness,
        "SurfaceArea": SurfaceArea,
        "WallArea": WallArea,
        "RoofArea": RoofArea,
        "OverallHeight": OverallHeight,
        "Orientation": Orientation,
        "GlazingArea": GlazingArea,
        "GlazingAreaDistribution": GlazingAreaDistribution
    }
    response = requests.post("http://api:5000/predict", json=input_data)

    # Mostrar o resultado
    if response.status_code == 200:
        result = response.json()
        st.success(f"Previsão da Carga de Aquecimento: {result['data']['prediction']:.2f} kWh/m²")
    else:
        st.error("Erro ao realizar a predição. Verifique os valores de entrada.")
