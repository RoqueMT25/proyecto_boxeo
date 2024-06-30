# Clasificación de Golpes de Boxeo

Este proyecto clasifica diferentes tipos de golpes de boxeo utilizando un modelo CNN+LSTM.

## Estructura del Proyecto

proyecto_boxeo/
│
├── notebooks/
│ ├── descarga_lista_videos.ipynb
│ ├── División fotogramas.ipynb
│ ├── Etiquetado_automático_sin_accion.ipynb
│ ├── Entrenar_modelo.ipynb
│
├── data/
│ ├── imagenes_test/
│ ├── imagenes_procesadas/
│ ├── etiquetas/
| ├── archivos_etiquetas.csv
│
├── modelos/
│ ├── path_to_saved_model.h5
│
├── app.py
│
├── requirements.txt
│
└── README.md


## Descripción del Proyecto

La idea principal era que un ordenador de 16 GB de RAM pudiera ejecutar este programa sin ningún problema, de ahí la reducción de la image_size.

Lo optimo sería aumentar el volumen de datos para que el modelo fuera más sólido.

El proyecto se divide en varias etapas, desde la descarga de videos de YouTube hasta el despliegue de una aplicación web para la clasificación de golpes de boxeo. A continuación se detallan las etapas principales:

### 1. Descarga de Videos de YouTube

En el notebook `1_descarga_videos_youtube.ipynb`, se descargan videos de YouTube que contienen secuencias de golpes de boxeo. Debido a la amplia gama de videos que se han descargado y se han tenido que guardar si han tenido que ir gusardando he ir modificando el código cada nada. Se han descargado videos de todo tipo y todas las épocas

### 2. División en Fotogramas

En el notebook `2_division_en_fotogramas.ipynb`, los videos descargados se dividen en fotogramas individuales para su posterior etiquetado y procesamiento. Se han tenido que ir borrando los fotogramas que no se iban a utilizar para dar paso a otros nuevos.

### 3. Etiquetado Automático y Manual

En el notebook `3_etiquetado_automatico_manual.ipynb`, se realiza el etiquetado automático y manual de los fotogramas. Este proceso es crucial para crear un conjunto de datos etiquetados para el entrenamiento del modelo. El 90 % de los datos se han etiquetado de manera manual para evitar errores. También se ha probado el etiquetado automático de las etiquetas "sin_accion" que no necesitaban un trato tan minucioso.

### 4. Entrenamiento del Modelo

En el notebook `4_entrena_modelo.ipynb`, se entrena un modelo CNN+LSTM utilizando los fotogramas etiquetados. El modelo se guarda en el archivo `modelo_entrenado.h5`. Ha sido muy complicado encontrar el mejor modelo adaptado a estos tipos de datos. pero los resultados han sido bastante destacables

### 5. Aplicación Streamlit

La aplicación `app.py` permite a los usuarios cargar imágenes y recibir predicciones sobre el tipo de golpe. La aplicación está construida con Streamlit.

## Requisitos

Instala las dependencias necesarias usando el archivo `requirements.txt`:

```sh
pip install -r requirements.txt

## Instrucciones

1. Clona el repositorio:
   ```sh
   git clone https://github.com/RoqueMT25/proyecto_boxeo.git
   cd proyecto_boxeo
