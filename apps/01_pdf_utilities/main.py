import streamlit as st

from merge import Merge
from split import Split
from protect import Protect

def main():
    st.header("Utilidades PDF")
    st.write("Aplicación desarrollada en streamlit que permite unir, dividir y proteger documentos pdf.")
    st.write("Desarrollada con <3 por dataSfar")

# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Inicio", "Unir PDFs", "Dividir PDF", "Proteger PDF"])

# Mostrar la página seleccionada
if pagina_actual == "Inicio":
    main()
elif pagina_actual == "Unir PDFs":
    merger = Merge()
    merger.merge_interface()
elif pagina_actual == "Dividir PDF":
    spliter = Split()
    spliter.split_interface()
elif pagina_actual == "Proteger PDF":
    protecter = Protect()
    protecter.protect_interface()

