import streamlit as st
import PyPDF2

from merge import Merge

# Variables
output_pdf = "pdf_final.pdf"
output_pdf_dividido = "pdf_dividido.pdf"
output_pdf_protected = "pdf_protected.pdf"

# Funciones
def unir_pdfs(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document)
    
    pdf_final.write(output_path)

def dividir_pdf(input_path, output_path, start_page, end_page):
    pdf_reader = PyPDF2.PdfReader(input_path)
    pdf_writer = PyPDF2.PdfWriter()

    for page_number in range(start_page, end_page+1):
        pdf_writer.add_page(pdf_reader.pages[page_number])
    
    with open(output_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

def proteger_pdf(input_path, output_path, password):
    pdf_reader = PyPDF2.PdfReader(input_path)
    pdf_writer = PyPDF2.PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
    
    with open(output_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

# Página para unir PDFs
def pagina_unir_pdfs():
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("assets/merge.png", width=200)
    st.header("Unir varios PDF's.")
    st.subheader("Adjuntar los pdfs a unir.")

    pdf_adjuntos = st.file_uploader(label="Unir PDFs", accept_multiple_files=True)

    unir = st.button(label="Unir PDF's")

    if unir:
        if len(pdf_adjuntos) <= 1:
            st.warning("Debes adjuntar más de un PDF")
        else:
            unir_pdfs(output_pdf, pdf_adjuntos)
            st.success("Clic aquí para descargar el PDF final")
            with open(output_pdf, "rb") as file:
                pdf_data = file.read()
            st.download_button(label="Descargar el PDF final", data=pdf_data, file_name="pdf_final.pdf")

# Página para dividir PDFs
def pagina_dividir_pdfs():
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("assets/split.png", width=200)
    st.header("Dividir archivos PDF")
    st.subheader("Abrir PDF a dividir")

    pdf_div = st.file_uploader(label="Dividir PDF", accept_multiple_files=False)

    if pdf_div is not None:
        pdf_reader = PyPDF2.PdfReader(pdf_div)
        num_paginas = len(pdf_reader.pages) 
        st.write(f"El PDF seleccionado tiene {num_paginas} páginas.")

        st.write("Dividir el PDF cada cuántas páginas:")
        paginas_por_dividir = st.number_input(label="Páginas por división", min_value=1, max_value=num_paginas, value=1)
        
        stop_here = num_paginas / paginas_por_dividir
        start_page = 0
        end_page = paginas_por_dividir - 1
        dividir = st.button(label="Dividir PDF")
        increment = 1

        if dividir:
            if pdf_div is not None:
                while stop_here>0:
                    stop_here-=1
                    dividir_pdf(pdf_div, output_pdf_dividido, start_page, end_page)
                    st.success("Clic aquí para descargar el PDF dividido")
                    with open(output_pdf_dividido, "rb") as file:
                        pdf_data = file.read()
                    st.download_button(label=f"Descargar el PDF dividido {increment}", data=pdf_data, file_name="pdf_dividido.pdf")
                    increment+=1
                    start_page = end_page + 1
                    end_page += paginas_por_dividir
                    if end_page >= num_paginas:
                        end_page = num_paginas - 1
            else:
                st.warning("Por favor, adjunta un PDF para dividir")

# Página para proteger PDFs con contraseña
def pagina_proteger_pdf():
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("assets/secure.png", width=200)
    st.header("Proteger archivo PDF")
    st.subheader("Selecciona un PDF para proteger con contraseña")

    pdf_prot = st.file_uploader(label="Proteger PDF")

    if pdf_prot is not None:
        password = st.text_input(label="Introduce la contraseña", type="password")
        confirm_password = st.text_input(label="Confirma la contraseña", type="password")
        
        if password == confirm_password and password != "":
            proteger = st.button(label="Proteger PDF")
            
            if proteger:
                proteger_pdf(pdf_prot, output_pdf_protected, password)
                st.success("Clic aquí para descargar el PDF protegido")
                with open(output_pdf_protected, "rb") as file:
                    pdf_data = file.read()
                st.download_button(label="Descargar el PDF protegido", data=pdf_data, file_name="pdf_protected.pdf")
        elif password != confirm_password and confirm_password != "":
            st.error("Las contraseñas no coinciden")

# Configuración de la barra lateral
pagina_actual = st.sidebar.radio("Utilidades", ["Unir PDFs", "Dividir PDF", "Proteger PDF", "Merger"])

# Mostrar la página seleccionada
if pagina_actual == "Unir PDFs":
    pagina_unir_pdfs()
elif pagina_actual == "Dividir PDF":
    pagina_dividir_pdfs()
elif pagina_actual == "Proteger PDF":
    pagina_proteger_pdf()
elif pagina_actual == "Merger":
    merger = Merge()
    merger.merge_interface()
