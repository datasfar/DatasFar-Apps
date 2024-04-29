import streamlit as st
import numpy as np
import cv2
from PIL import Image

class Transform():
    """
    Clase para cambiar el tamaño de una imagen y proporcionar una interfaz web para hacerlo.
    """

    def __init__(self) -> None:
        """
        Inicializa la clase Transform.
        """
        self.output_img = "imagen_final.png"


    def transform_img(self, image, width, height):  
        """
        Cambia el tamaño de una imagen.

        Parámetros:
        image (file): La imagen a cambiar de tamaño.
        width (int): El ancho deseado de la imagen.
        height (int): La altura deseada de la imagen.
        """
        try:
            img = Image.open(image)
            img = np.array(img)
            img = cv2.resize(img, (width, height))
            img = Image.fromarray(img)
            img.save(self.output_img)
        except Exception as e:
            st.error(f"Error al cambiar el tamaño de la imagen: {e}")


    def show_info(self, image):
        """
        Muestra información de la imagen original.

        Parámetros:
        image (file): La imagen de la cual se mostrará la información.
        """

        try:
            img = Image.open(image)
            st.image(img, caption='Imagen Original', width=240)
            st.write(f'Dimensiones de la imagen original: {img.size}')
        except Exception as e:
            st.error(f"Error al mostrar información de la imagen: {e}")


    def transform_interface(self):
        """
        Genera la interfaz web para cambiar el tamaño de una imagen.
        """
        
        st.header("Cambiar Tamaño de la Imagen")
        st.subheader("Adjunta la imagen a la que desea cambiar el tamaño")

        image = st.file_uploader(label="Cambiar Tamaño de la Imagen", type=["jpg", "jpeg", "png"])

        if image is not None:
            self.show_info(image)

        options = st.selectbox("Seleccionar tamaño predefinido", ["Seleccionar", "1920 × 1080", "1280 × 720", "854 × 480", "640 × 360", "426 × 240"])

        if options != "Seleccionar":
            width, height = map(int, options.split(" × "))
        else:
            width = st.slider("Ancho", 50, 1920, 890)
            height = st.slider("Altura", 50, 1920, 890)


        transform_action = st.button(label="Cambiar Tamaño")

        if transform_action:
            if image is None:
                st.warning("Debes subir una imagen")
            else:
                self.transform_img(image, width, height)
                st.success("¡Imagen cambiada de tamaño exitosamente!")
                try:
                    with open(self.output_img, "rb") as file:
                        image = file.read()
                    st.download_button(label="Descargar la imagen cambiada de tamaño", data=image, file_name="imagen_resized.png")
                except FileNotFoundError as e:
                    st.error(f"Error al descargar la imagen: {e}")