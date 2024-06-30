
import streamlit as st
import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model

# Cargar el modelo
model = load_model('modelos/modelo_entrenado.h5')

# Configuración de la aplicación
st.title("Clasificación de Golpes de Boxeo")
st.write("Esta aplicación clasifica diferentes tipos de golpes de boxeo utilizando un modelo CNN+LSTM.")

# Cargar y preprocesar imagen
uploaded_file = st.file_uploader("Elija una imagen...", type="jpg")

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption='Imagen subida.', use_column_width=True)

    # Normalizar imagen
    image = image / 255.0

    # Crear una secuencia replicando la imagen
    seq_length = 10
    sequence = np.repeat(np.expand_dims(image, axis=0), seq_length, axis=0)
    sequence = np.expand_dims(sequence, axis=0)  # Añadir dimensión para el batch

    # Hacer predicción
    pred = model.predict(sequence)
    pred_class = np.argmax(pred, axis=1)

    # Mapear la predicción a la etiqueta correspondiente
    label_mapping = {
        0: "bloqueo",
        1: "crochet",
        2: "cross",
        3: "esquiva",
        4: "hook",
        5: "jab",
        6: "overhand",
        7: "sin_accion",
        8: "uppercut"
    }
    prediction = label_mapping[pred_class[0]]
    st.write(f"Predicción: {prediction}")