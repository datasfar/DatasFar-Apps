# Importamos las librerias
import streamlit as st

from convert import Convert 
from text_to_audio import Text_to_audio
from audio_to_text import Audio_to_text
from image_to_text import Image_to_text

def main():
    st.header("Aplicación con utilidades para manejar textos")
    st.write("La aplicación permite extraer texto de imagenes y audios y generar audios a partir de texto plano")
    st.write("Desarrollada con <3 por dataSfar")


# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Inicio", "Imagen a Texto", "Audio a Texto", "Texto a Audio", "Convertir a .wav"])

# Mostrar la página seleccionada
if pagina_actual == "Inicio":
    main()
elif pagina_actual == "Imagen a Texto":
    text_extractor_from_image = Image_to_text()
    text_extractor_from_image.text_extractor_interface()
elif pagina_actual == "Audio a Texto":
    text_extractor_from_audio = Audio_to_text()
    text_extractor_from_audio.text_extractor_interface()
elif pagina_actual == "Texto a Audio":
    audio_generator = Text_to_audio()
    audio_generator.text_to_audio_interface()
elif pagina_actual == "Convertir a .wav":
    converter = Convert()
    converter.convert_interface()
