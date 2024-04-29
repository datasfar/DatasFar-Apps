import streamlit as st

from convert import Convert
from transform import Transform
from bg_remove import Bg_Remove

def main():
    st.header("Aplicación con utilidades para imagenes")
    st.write("Permite convertir, redimensionar y eliminar el fondo de las imagenes.")
    st.write("Desarrollado con <3 por dataSfar")

# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Inicio", "Convertir Imagen", "Cambiar Tamaño", "Eliminar Fondo"])

# Mostrar la página seleccionada
if pagina_actual == "Inicio":
    main()
elif pagina_actual == "Convertir Imagen":
    converter = Convert()
    converter.convert_interface()
elif pagina_actual == "Cambiar Tamaño":
    transformer = Transform()
    transformer.transform_interface()
elif pagina_actual == "Eliminar Fondo":
    remover = Bg_Remove()
    remover.remove_interface()
