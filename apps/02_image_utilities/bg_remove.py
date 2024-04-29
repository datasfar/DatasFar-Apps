import streamlit as st
from io import BytesIO
from rembg import remove
from PIL import Image

class Bg_Remove():
    """
    Clase para eliminar el fondo de una imagen y proporcionar una interfaz web para hacerlo.
    """

    def __init__(self) -> None:
        """
        Inicializa la clase Bg_Remove.
        """
        pass


    def preprocess_img(self, image):
        """
        Preprocesa la imagen para su procesamiento.

        Parámetros:
        image (PIL.Image): La imagen a procesar.

        Retorna:
        bytes: La imagen preprocesada en formato bytes.
        """

        try:
            buf = BytesIO()
            image.save(buf, format="PNG")
            byte_img = buf.getvalue()
            return byte_img
        except Exception as e:
            st.error(f"Error al preprocesar la imagen: {e}")
            return None
    
    
    def remove_interface(self):
        """
        Genera la interfaz web para eliminar el fondo de una imagen.
        """

        st.header("Eliminar el fondo de una imagen.")
        st.subheader("Adjuntar la imagen a la que quieres eliminar el fondo.")

        image_upload = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

        if image_upload is not None:
            try:
                image = Image.open(image_upload)
                fixed = remove(image)
                downloadable_image = self.preprocess_img(fixed)
                if downloadable_image:
                    st.image(fixed, caption='Imagen procesada', use_column_width=True)
                    st.download_button("Descargar imagen procesada", downloadable_image, "imagen_procesada.png", "image/png")
            except Exception as e:
                st.error(f"Error al procesar la imagen: {e}")