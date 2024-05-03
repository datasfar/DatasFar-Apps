import streamlit as st
from pytube import YouTube

# Ya no es necesario el ssl (?)
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class Downloader():
    
    def video_downloader_interface(self):

        url = st.text_input("Inserte la url")
        audio = st.checkbox("Descargar solo el audio ",)
        download_button = st.button("Descargar")

        if url != "":
            youtube = YouTube(url)

            # extras
            col1, col2 = st.columns(2)

            with col1:
                st.write(youtube.title, "Subido por:", youtube.author)
                st.write(str(youtube.views), "views")
                st.write("Subido el:", str(youtube.publish_date))
                st.write("Duración: ", youtube.length, "sec")

            with col2:
                st.image(youtube.thumbnail_url)

        if download_button:

            if audio == True:
                video = youtube.streams.get_audio_only()
                video.download("./Descargas")
                st.success("Audio descargado correctamente")
            else:
                video = youtube.streams.get_highest_resolution()
                video.download("./Descargas")
                st.success("Video descargado correctamente")
            