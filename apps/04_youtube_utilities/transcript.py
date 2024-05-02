import streamlit as st
# No funcionan los caption con pytube, buscar alternativa

class Transcripter():
      
    def video_transcript_interface(self):

        st.header("Descargar videos de Youtube")
        url = st.text_input("Inserte la url")

       

