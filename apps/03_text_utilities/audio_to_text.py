import streamlit as st
import speech_recognition as sr

class Audio_to_text():

    def __init__(self) -> None:
        pass

    def text_extractor(self, audio_file, selected_language):
        """
        Convierte un archivo de audio en texto utilizando reconocimiento de voz.

        Parámetros:
        archivo_audio (file): El archivo de audio a convertir.
        selected_language (str): El idioma del texto.

        Retorna:
        str: El texto convertido.
        """
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as fuente:
            audio = recognizer.record(fuente)
            try:
                text = recognizer.recognize_google(audio, language=selected_language)
                return text
            
            except sr.UnknownValueError:
                return "No se pudo entender el audio"
            
            except sr.RequestError as e:
                return f"Error: {str(e)}"
            
    def text_extractor_interface(self):
        """
        Genera la interfaz web para convertir voz a texto.
        """
        st.title("Convertidor de Voz a Texto")
        st.write("Cargue un archivo de audio .wav y conviértalo en texto.")

        selected_language = st.radio("Selecciona el idioma",["es-ES", "en-EN"])
        audio_uploaded = st.file_uploader("Elija un archivo de audio", type=["wav"])

        if audio_uploaded is not None:

            try:
                file_details = {"Nombre del archivo": audio_uploaded.name, "Tipo de archivo": audio_uploaded.type}
                st.write(file_details)
                st.audio(audio_uploaded)
                text = self.text_extractor(audio_uploaded, selected_language)
                st.write("Texto convertido:")
                st.write(text)

            except Exception as e:
                st.error(f"Error al convertir el audio a texto: {e}")
