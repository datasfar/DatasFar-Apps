import streamlit as st

class Convert():
    """
    Clase para convertir un archivo de audio a formato .wav y proporcionar una interfaz web para hacerlo.
    """

    def __init__(self) -> None:
        """
        Inicializa la clase Convert.
        """
        pass


    def convert_interface(self):
        """
        Genera la interfaz web para convertir un archivo de audio a formato .wav.
        """
        st.warning("Esta funcionalidad no ha sido implementada todavía.")
        st.title("Convertir archivo de audio a .wav")
        st.write("Adjunte un archivo de audio en formato .ogg y conviértalo a .wav.")

        audio_uploaded = st.file_uploader("Elija un archivo de audio", type=["ogg"])

        if audio_uploaded is not None:

            try:
                file_details = {"Nombre del archivo": audio_uploaded.name, "Tipo de archivo": audio_uploaded.type}
                st.write(file_details)

                st.audio(audio_uploaded)
                st.download_button(label="Descargar audio", data=audio_uploaded , file_name="audio.wav")

            except Exception as e:
                st.error(f"Error al procesar el archivo de audio: {e}")

