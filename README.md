# 🫀 Predictor de Problemas Cardíacos

Esta es una aplicación en **Streamlit** que permite predecir si una persona puede sufrir de problemas cardíacos, en función de su **edad** y **nivel de colesterol**.  

El modelo utilizado es un **SVC (Support Vector Classifier)** previamente entrenado y normalizado con **MinMaxScaler**. Ambos fueron guardados con `joblib`.

---

## 📌 Características
- Predice si una persona:
  - **0 → No sufrirá del corazón**  
  - **1 → Sí sufrirá del corazón**  
- Interfaz amigable con **sliders** para ingresar:
  - Edad (25 a 80 años, por defecto 55, incrementos de 1)  
  - Colesterol (120 a 600, por defecto 242, incrementos de 2)  
- Muestra imágenes dependiendo del resultado:
  - ✅ Imagen positiva si no sufrirá del corazón.  
  - ⚠️ Imagen negativa si sufrirá del corazón.  
- Incluye título y subtítulo de autoría.

---

## 📂 Estructura del proyecto
├── app.py # Aplicación principal en Streamlit
├── modelo_svc.jb # Modelo entrenado SVC (joblib)
├── scaler.jb # Scaler (MinMaxScaler) usado en entrenamiento
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación del proyecto


---

## ▶️ Cómo ejecutar la aplicación

1. Clonar este repositorio o copiar los archivos a tu proyecto.  

2. Instalar dependencias:
   ```bash
   
---

¿Quieres que también te genere un **ejemplo de dataset sintético y entrenamiento del modelo `modelo_svc.jb` y `scaler.jb`** para que puedas correr la app sin necesidad de datos externos?

   pip install -r requirements.txt


streamlit run app.py
