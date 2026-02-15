# 🏠 Predicción de Precios de Viviendas con IA

Este proyecto utiliza **Machine Learning** para analizar y predecir el precio de inmuebles basándose en características como el área (m²), número de habitaciones y equipamiento.

## 📊 Análisis de Datos
Durante la exploración inicial, convertimos las unidades a **metros cuadrados** y escalamos los precios a **millones** para facilitar la lectura.

### Hallazgos clave:
* Existe una correlación directa entre el tamaño de la casa y su valor.
* El **aire acondicionado** es un factor determinante en el precio final, incluso en casas de igual tamaño.

## 🤖 El Modelo de IA
Se implementó un modelo de **Regresión Lineal** utilizando `Scikit-Learn`.
* **Variables usadas:** Area ($m^2$), Habitaciones, Baños y Aire Acondicionado.
* **Estado:** Entrenado y listo para predicciones.

## 🛠️ Tecnologías utilizadas
* **Python** (Lógica principal)
* **Pandas** (Gestión de datos)
* **Matplotlib/Seaborn** (Visualizaciones)
* **Scikit-Learn** (Inteligencia Artificial)