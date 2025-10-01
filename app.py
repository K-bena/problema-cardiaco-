import streamlit as st
import joblib
import numpy as np

# Cargar modelo y scaler
model = joblib.load("modelo_svc.jb")   # archivo del modelo
scaler = joblib.load("scaler.jb")      # archivo del escalador

# Configuración de la app
st.title("🫀 Predictor de problemas cardiacos")
st.subheader("Elaborado por **unab2025**")

# Sliders para la edad y el colesterol
edad = st.slider(
    "Seleccione la edad:",
    min_value=25,
    max_value=80,
    value=55,         # por defecto
    step=1            # de uno en uno
)

colesterol = st.slider(
    "Seleccione el nivel de colesterol:",
    min_value=120,
    max_value=600,
    value=242,        # por defecto
    step=2            # de dos en dos
)

# Botón de predicción
if st.button("Predecir"):
    # Preparar los datos
    X = np.array([[edad, colesterol]])
    X_scaled = scaler.transform(X)

    # Predicción
    pred = model.predict(X_scaled)[0]

    if pred == 0:
        st.success("✅ La persona NO sufrirá del corazón")
        st.image("https://img.freepik.com/foto-gratis/feliz-mujer-atractiva-bailando-divirtiendose-levantando-manos-preocupaciones-disfrutando-musica-pie-contra-pared-blanca_176420-38816.jpg?semt=ais_hybrid&w=740&q=80", width=400)
    else:
        st.error("⚠️ La persona SÍ sufrirá del corazón")
        st.image("https://www.shutterstock.com/image-vector/unwell-man-feel-sick-suffer-600nw-2145831019.jpg", width=400)
