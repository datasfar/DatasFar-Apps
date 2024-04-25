# Importamos las librerias
import streamlit as st
from gtts import gTTS
import io
from io import BytesIO
import base64
import speech_recognition as sr
from pydub import AudioSegment
import soundfile as sf


# Función para convertir texto a audio
def texto_a_audio():
    st.title("Convertidor de Texto a Audio")
    st.write("Escribe un texto y conviértelo en audio.")

    selected_language = st.radio("Selecciona el idioma:", ["es", "en"])
    texto = st.text_area("Ingrese el texto:")

    if st.button("Convertir a audio"):
        # Convertir texto a audio
        tts = gTTS(texto, lang=selected_language)
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        st.audio(audio, format='audio/wav')

        # Descargar el archivo de audio
        audio_descargable = audio.getvalue()
        st.download_button(label="Descargar audio",data=audio_descargable, file_name="audio.wav")

# Función para convertir voz a texto utilizando reconocimiento de voz
def voz_a_texto(archivo_audio, selected_language='es-ES'):
    reconocedor = sr.Recognizer()
    with sr.AudioFile(archivo_audio) as fuente:
        audio = reconocedor.record(fuente)
        try:
            texto = reconocedor.recognize_google(audio, language=selected_language)
            return texto
        except sr.UnknownValueError:
            return "No se pudo entender el audio"
        except sr.RequestError as e:
            return f"Error: {str(e)}"


# Función para la vista convertir voz a texto
def audio_a_texto():
    st.title("Convertidor de Voz a Texto")
    st.write("Cargue un archivo de audio .wav y conviértalo en texto.")

    selected_language = st.radio("Selecciona el idioma",["es-ES", "en-EN"])
    archivo_cargado = st.file_uploader("Elija un archivo de audio", type=["wav"])

    if archivo_cargado is not None:
        detalles_archivo = {"Nombre del archivo": archivo_cargado.name, "Tipo de archivo": archivo_cargado.type}
        st.write(detalles_archivo)

        st.audio(archivo_cargado)
        texto = voz_a_texto(archivo_cargado, selected_language)
        st.write("Texto convertido:")
        st.write(texto)

# Función para convertir el audio a .wav
def convertir_wav():
    st.title("Convertir archivo de audio a .wav")
    st.write("Cargue un archivo de audio en formato .ogg y conviértalo a .wav.")

    archivo_cargado = st.file_uploader("Elija un archivo de audio", type=["ogg"])

    if archivo_cargado is not None:
        detalles_archivo = {"Nombre del archivo": archivo_cargado.name, "Tipo de archivo": archivo_cargado.type}
        st.write(detalles_archivo)

        st.audio(archivo_cargado)
        st.download_button(label="Descargar audio", data=archivo_cargado , file_name="audio.wav")



# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Audio a Texto", "Texto a Audio", "Convertir a .wav"])

# Mostrar la página seleccionada
if pagina_actual == "Audio a Texto":
    audio_a_texto()
elif pagina_actual == "Texto a Audio":
    texto_a_audio()
elif pagina_actual == "Convertir a .wav":
    convertir_wav()
