import streamlit as st
from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class Downloader():
    
    def video_downloader_interface(self):

        st.header("Descargar videos de Youtube")
        url = st.text_input("Inserte la url")
        resolution = st.selectbox("Selecciona la resolución",["720p","480p","360p", "240p","144p"])

        download_button = st.button("Descargar")

        if download_button:
            
            youtube = YouTube(url)

            video = youtube.streams.get_by_resolution(resolution)
            video.download("./Descargas")
            st.success("Video descargado con exito")

