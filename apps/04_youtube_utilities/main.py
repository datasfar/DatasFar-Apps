import streamlit as st

from downloader import Downloader
from transcript import Transcripter


def main():
    st.header("Aplicación para descargar videos de Youtube")
    st.write("Descarga y analiza videos de youtube")
    st.write("Desarrollada con <3 por dataSfar")

# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Inicio", "Descargador", "Transcript"])

# Mostrar la página seleccionada
if pagina_actual == "Inicio":
    main()
elif pagina_actual == "Descargador":
    video_downloader = Downloader()
    video_downloader.video_downloader_interface()
elif pagina_actual == "Transcript":
    video_transcript = Transcripter()
    video_transcript.video_transcript_interface()

