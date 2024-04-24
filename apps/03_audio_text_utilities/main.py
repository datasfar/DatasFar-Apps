# Importamos las librerias
import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment


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

# Función principal que define la interfaz de usuario
def main():
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

if __name__ == "__main__":
    main()

'''
import os,sys

orig_song = sys.argv[1]
dest_song = os.path.splitext(sys.argv[1])[0]+'.wav'

def convert_ogg_to_wav():
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="wav")
    
if __name__ == '__main__':
    convert_ogg_to_wav()
'''