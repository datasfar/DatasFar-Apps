import streamlit as st
from PIL import Image

class Convert():
    """
    Clase para convertir una imagen a formato PNG y proporcionar una interfaz web para hacerlo.
    """


    def __init__(self) -> None:
        """
        Inicializa la clase Convert.
        """

        self.output_img = "imagen_final.png"


    def convert_img(self, image):
        """
        Convierte una imagen a formato PNG.

        Parámetros:
        image (file): La imagen a convertir.
        """

        try:
            img = Image.open(image)
            img.save(self.output_img, format='PNG')
        except Exception as e:
            st.error(f"Error al convertir la imagen: {e}")


    def convert_interface(self):
        """
        Genera la interfaz web para convertir una imagen a formato PNG.
        """

        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image("assets/convert.png", width=200)
        st.header("Cambiar tamaño de una imagen")
        st.subheader("Sube la imagen a convertir")

        image = st.file_uploader(label="Imagen a convertir", type=["jpg", "jpeg"])

        convert_action = st.button(label="Convertir")

        if convert_action:
            if image is None:
                st.warning("Debes subir una imagen")
            else:
                self.convert_img(image)
                st.success("¡Imagen convertida exitosamente!")
                try:
                    with open(self.output_img, "rb") as file:
                        image = file.read()
                    st.download_button(label="Descargar la imagen convertida", data=image, file_name="imagen_final.png")
                except FileNotFoundError as e:
                    st.error(f"Error al descargar la imagen: {e}")