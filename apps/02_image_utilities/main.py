import streamlit as st
from PIL import Image
import cv2
import numpy as np

### CONVERTIR IMAGEN

def convertir_img(imagen, output):
    img = Image.open(imagen)
    img.save(output, format='PNG')

def jpg_to_png():
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("assets/convert.png", width=200)
    st.header("Cambiar tamaño de una imagen")
    st.subheader("Sube la imagen a modificar")

    imagen = st.file_uploader(label="Imagen a transformar", type=["jpg", "jpeg"])
    output = "imagen.png"

    convertir = st.button(label="Transformar")

    if convertir:
        if imagen is None:
            st.warning("Debes subir una imagen")
        else:
            convertir_img(imagen, output)
            st.success("¡Imagen transformada exitosamente!")
            with open(output, "rb") as file:
                imagen = file.read()
            st.download_button(label="Descargar la imagen transformada", data=imagen, file_name="imagen.png")


### TRANSFORMAR IMAGEN

def transformar_img(imagen, output, width, height):
    img = Image.open(imagen)
    img = np.array(img)
    img = cv2.resize(img, (width, height))
    img = Image.fromarray(img)
    img.save(output)

def mostrar_info(imagen):
    img = Image.open(imagen)
    st.image(img, caption='Imagen Original', width=240)
    st.write(f'Dimensiones de la imagen original: {img.size}')

def cambiar_tamaño():
    st.header("Cambiar Tamaño de la Imagen")
    st.subheader("Sube la imagen a cambiar de tamaño")

    imagen = st.file_uploader(label="Cambiar Tamaño de la Imagen", type=["jpg", "jpeg", "png"])
    output = "imagen_resized.png"

    if imagen is not None:
        mostrar_info(imagen)

    opcion = st.selectbox("Seleccionar tamaño predefinido", ["Seleccionar", "1920 × 1080", "1280 × 720", "854 × 480", "640 × 360", "426 × 240"])

    if opcion != "Seleccionar":
        width, height = map(int, opcion.split(" × "))
    else:
        width = st.slider("Ancho", 50, 1920, 890)
        height = st.slider("Altura", 50, 1920, 890)


    cambiar = st.button(label="Cambiar Tamaño")

    if cambiar:
        if imagen is None:
            st.warning("Debes subir una imagen")
        else:
            transformar_img(imagen, output, width, height)
            st.success("¡Imagen cambiada de tamaño exitosamente!")
            with open(output, "rb") as file:
                imagen = file.read()
            st.download_button(label="Descargar la imagen cambiada de tamaño", data=imagen, file_name="imagen_resized.png")

### ELIMINAR BACKGROUNDS

# Importamos librerias
from io import BytesIO
#No es compatible con Python 3.12
from rembg import remove

# Convierte la imagen a ByteIO para procesarla
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def eliminar_fondo():
    st.header("Eliminar el fondo de una imagen.")
    st.subheader("Adjuntar la imagen a la que quieres eliminar el fondo.")

    # Subir la imagen
    image_upload = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

    # Cuando subimos la imagen la abre y la procesa
    if image_upload is not None:
        image = Image.open(image_upload)
        fixed = remove(image)
        downloadable_image = convert_image(fixed)
        st.image(fixed, caption='Imagen procesada', use_column_width=True)
        st.download_button(
            "Descargar imagen procesada", downloadable_image, "imagen_procesada.png", "image/png"
        )

# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Convertir Imagen", "Cambiar Tamaño", "Eliminar Fondo"])

# Mostrar la página seleccionada
if pagina_actual == "Convertir Imagen":
    jpg_to_png()
elif pagina_actual == "Cambiar Tamaño":
    cambiar_tamaño()
elif pagina_actual == "Eliminar Fondo":
    eliminar_fondo()
