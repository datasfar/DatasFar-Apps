import streamlit as st
from gtts import gTTS
import io

class Text_to_audio():
    """
    Clase para convertir un texto en audio.
    """

    def __init__(self) -> None:
        """
        Inicializador de la clase Text_to_audio
        """
        pass


    def audio_generator(self, text, selected_language):
        """
        Genera el archivo de audio a partir del texto proporcionado.

        Parámetros:
        texto (str): El texto a convertir en audio.
        selected_language (str): El idioma del texto.

        Retorna:
        io.BytesIO: El archivo de audio en formato BytesIO.
        """

        tts = gTTS(text, lang=selected_language)
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        return audio


    def text_to_audio_interface(self):
        """
        Genera la interfaz web para convertir texto a audio.
        """

        st.title("Convertidor de Texto a Audio")
        st.write("Escribe un texto que desea convertir en audio.")

        selected_language = st.radio("Selecciona el idioma:", ["es", "en"])
        text = st.text_area("Ingrese el texto:")

        if st.button("Convertir a audio"):

            try:
                audio = self.audio_generator(text, selected_language)
                st.audio(audio, format='audio/wav')
                generated_audio = audio.getvalue()
                st.download_button(label="Descargar audio",data=generated_audio, file_name="audio_generado.wav")

            except Exception as e:
                st.error(f"Error al convertir el texto a audio: {e}")
