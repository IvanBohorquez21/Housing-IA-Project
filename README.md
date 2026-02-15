# 🏡 Housing IA Project - Predicción de Precios

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

Este proyecto utiliza **Machine Learning** para predecir el precio de viviendas basándose en características como el área, número de habitaciones, baños y servicios adicionales.

---

## 📊 Origen de los Datos

Los datos utilizados en este proyecto fueron obtenidos de **Kaggle**, específicamente del dataset  
**[Housing Price Prediction](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)**.

El dataset original fue procesado para normalizar unidades de medida y transformar variables categóricas para el entrenamiento de los modelos.

---

## 🚀 Logros del Proyecto

- **Mejor Modelo**: Regresión Lineal con una precisión del **58.67% (R²)**.
- **Experimentación**: Se comparó con **Random Forest Regressor** (56.62%) para validar el rendimiento, concluyendo que para este volumen de datos, el modelo lineal generaliza mejor.
- **Procesamiento de Datos**:
  - Conversión de unidades (Sqft a m²)
  - Tratamiento de valores nulos
  - Codificación de variables categóricas (One-Hot Encoding)
- **Visualización Avanzada**: Gráficos con formato de moneda (Millones de $) y comparativas de rendimiento.

---

## 📖 Diccionario de Datos

| Columna | Descripción |
|----------|------------|
| **area_m2** | Tamaño de la vivienda convertido a metros cuadrados. |
| **bedrooms** | Cantidad de habitaciones. |
| **bathrooms** | Número de baños completos. |
| **airconditioning_num** | Presencia de aire acondicionado (1: Sí, 0: No). |
| **parking** | Capacidad de estacionamiento (número de vehículos). |
| **price** | Precio de venta final (Variable objetivo). |

---

## 📊 Visualización de Resultados

### Precisión del Modelo Ganador (Lineal)

Aquí se muestra cómo el modelo de Regresión Lineal predice los precios frente a los valores reales:

![Gráfico de Predicciones](img/grafico_resultados.png)

### Comparativa: Lineal vs. Random Forest

Análisis de rendimiento entre un modelo simple y uno complejo:

![Duelo de Modelos](img/comparativa_modelos.png)

---

## 🛠️ Instalación y Uso

Para replicar este proyecto localmente, sigue estos pasos:

### 1 Clonar el repositorio

```bash
git clone https://github.com/IvanBohorquez21/Housing-IA-Project.git
```

### 2️ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️ Ejecutar los Notebooks

Abre VS Code o Jupyter Notebook y ejecuta los archivos en este orden:


    01_analisis_exploratorio.ipynb
    02_entrenamiento_modelo.ipynb
    03_mejora_modelo_rf.ipynb


---

## 📁 Estructura del Repositorio


    /data       → Dataset original de precios de vivienda
    /notebooks  → Procesos de análisis, limpieza y entrenamiento
    /models     → Modelos entrenados en formato .pkl listos para producción
    /img        → Gráficos y visualizaciones generadas para el análisis


---

Proyecto desarrollado como parte de un flujo de aprendizaje en Ciencia de Datos.
