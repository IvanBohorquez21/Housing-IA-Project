# 🏡 Housing IA Project - Predicción de Precios

Este proyecto utiliza **Machine Learning** para predecir el precio de viviendas basándose en características como el área, número de habitaciones, baños y servicios adicionales.

## 📊 Origen de los Datos
Los datos utilizados en este proyecto fueron obtenidos de **Kaggle**, específicamente del dataset **[Housing Price Prediction](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)**. 

Este conjunto de datos contiene información detallada sobre el mercado inmobiliario, incluyendo variables críticas como el área total, el número de habitaciones, baños, pisos, y comodidades adicionales (aire acondicionado, estacionamiento, etc.) que influyen en el precio final de las viviendas.

## 🚀 Logros del Proyecto
* **Mejor Modelo**: Regresión Lineal con una precisión del **58.67% ($R^2$)**.
* **Experimentación**: Se comparó con **Random Forest Regressor** (56.62%) para validar el rendimiento.
* **Procesamiento de Datos**: Conversión de unidades (Sqft a m²), tratamiento de valores nulos y codificación de variables categóricas.
* **Visualización Avanzada**: Gráficos con formato de moneda (Millones de $) y comparativas de modelos.

## 📊 Visualización de Resultados

### Precisión del Modelo Ganador (Lineal)
![Gráfico de Predicciones](grafico_resultados.png)

### Comparativa: Lineal vs. Random Forest
![Duelo de Modelos](comparativa_modelos.png)

## 🛠️ Tecnologías Usadas
* **Python**: Pandas, Scikit-Learn
* **Visualización**: Matplotlib & Seaborn
* **Persistencia**: Joblib para guardar modelos `.pkl`
* **Git & GitHub**: Control de versiones y despliegue de portafolio.

## 📁 Estructura del Repositorio
* `/data`: Dataset original de precios de vivienda.
* `/notebooks`: 
    * `01_analisis_exploratorio.ipynb`
    * `02_entrenamiento_modelo.ipynb`
    * `03_mejora_modelo_rf.ipynb` (Nuevos experimentos)
* `/models`: 
    * `house_price_model.pkl` (Modelo Ganador)
    * `random_forest_model.pkl` (Modelo Experimental)
    * `model_columns.pkl` (Variables de entrada)

---
*Proyecto desarrollado como parte de un flujo de aprendizaje en Ciencia de Datos.*