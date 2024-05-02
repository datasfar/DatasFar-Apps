import streamlit as st

from downloader import Downloader


def main():
    st.header("Aplicación para corregir & traducir textos.")
    st.write("La aplicación permite corregir la ortografía y traducir textos.")
    st.write("Desarrollada con <3 por dataSfar")

# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Inicio", "Descargador", "Traductor"])

# Mostrar la página seleccionada
if pagina_actual == "Inicio":
    main()
elif pagina_actual == "Descargador":
    video_downloader = Downloader()
    video_downloader.video_downloader_interface()

