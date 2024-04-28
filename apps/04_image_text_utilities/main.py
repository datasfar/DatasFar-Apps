import streamlit as st
import pytesseract
from PIL import Image

def main():
    st.title("Convertidor de imagen a texto")
    st.write("Sube tu imagen con texto")

    imagen_cargada = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    if imagen_cargada is not None:

        image = Image.open(imagen_cargada)
        text = pytesseract.image_to_string(image)
        st.image(imagen_cargada)
        st.write(text)

main()