import streamlit as st
import pytesseract
from PIL import Image

class Image_to_text():
    """
    Clase para convertir una imagen a texto utilizando OCR (Reconocimiento Óptico de Caracteres).
    """

    def __init__(self) -> None:
        """
        Inicializa la clase Image_to_text.
        """
        pass


    def text_extractor(self, image):
        """
        Convierte una imagen a texto utilizando OCR (Reconocimiento Óptico de Caracteres).
        
        Parámetros:
        image (PIL.Image): La imagen a convertir.
        """

        if image is not None:
            try:
                text = pytesseract.image_to_string(image)
                st.image(image)
                st.write(text)
            except Exception as e:
                st.error(f"Error al procesar la imagen: {e}")


    def text_extractor_interface(self):
        """
        Genera la interfaz web para cargar una imagen.
        
        Retorna:
        PIL.Image: La imagen cargada.
        """

        st.title("Convertidor de imagen a texto")
        st.write("Sube tu imagen con texto")

        image_uploaded = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

        if image_uploaded is not None:
            try:
                image = Image.open(image_uploaded)
                self.text_extractor(image)
            except Exception as e:
                st.error(f"Error al cargar la imagen: {e}")
                return None