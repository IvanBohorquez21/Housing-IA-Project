import streamlit as st
import pandas as pd
import os
import joblib

# 1. Configuración de la página
st.set_page_config(page_title="IA Predicción de Vivienda", page_icon="🏠")

# 2. Cargar el modelo
# Usamos una ruta relativa que funcione tanto en tu PC como en la nube
modelo_path = os.path.join('models', 'modelo_vivienda_v2.pkl')

if os.path.exists(modelo_path):
    modelo = joblib.load(modelo_path)
else:
    st.error("❌ No se encontró el modelo en la carpeta 'models'.")

# 3. Interfaz de usuario
st.title("🏠 Simulador de Precios de Vivienda")
st.write("Mueve los controles para calcular el precio estimado de una propiedad.")

with st.sidebar:
    st.header("Características de la Casa")
    area = st.number_input("Área total (m²)", min_value=10, max_value=1000, value=150)
    habitaciones = st.slider("Dormitorios", 1, 6, 3)
    banos = st.slider("Baños", 1, 4, 2)
    parking = st.slider("Plazas de Garaje", 0, 3, 1)
    aire = st.radio("¿Tiene Aire Acondicionado?", ["No", "Sí"])

# 4. Procesamiento de los datos (Igual que en el notebook 04)
# Convertir aire a numérico
aire_num = 1 if aire == "Sí" else 0

# Crear las variables de ingeniería (Feature Engineering)
servicios_total = aire_num + parking
amplitud_habitacion = area / habitaciones
es_premium = 1 if (banos > 1 and aire_num == 1) else 0

# Crear el DataFrame para pasarle al modelo
# ¡IMPORTANTE!: Las columnas deben estar en el mismo orden que cuando entrenaste
columnas = ['area_m2', 'bedrooms', 'bathrooms', 'parking', 'servicios_total', 'amplitud_habitacion', 'es_premium']
input_df = pd.DataFrame([[area, habitaciones, banos, parking, servicios_total, amplitud_habitacion, es_premium]], 
                        columns=columnas)

# 5. Predicción y visualización
if st.button("Calcular Precio"):
    prediccion = modelo.predict(input_df)
    precio_final = prediccion[0]
    
    st.success(f"### 💰 Precio Estimado en USD: ${precio_final:,.2f}")
    
    # Un toque extra: comparar con el promedio
    st.info(f"Este modelo utiliza las 3 variables nuevas que creaste: Servicios, Amplitud y Premium.")