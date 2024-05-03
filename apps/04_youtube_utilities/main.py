import streamlit as st

from downloader import Downloader


def main():

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("./assets/yt.png")

    st.header("Aplicación para descargar videos de Youtube")

    video_downloader = Downloader()
    video_downloader.video_downloader_interface()

    col1, col2, col3 = st.columns(3)
    with col3:
        st.write("Desarrollada con ❤️ por dataSfar")



main()

