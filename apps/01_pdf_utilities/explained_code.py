import streamlit as st  # Importa la librería Streamlit para construir aplicaciones web interactivas
import PyPDF2  # Importa la librería PyPDF2 para trabajar con archivos PDF

# Variables para los nombres de los archivos PDF de salida
output_pdf = "pdf_final.pdf"
output_pdf_dividido = "pdf_dividido.pdf"
output_pdf_protected = "pdf_protected.pdf"

# Función para unir varios PDFs en uno solo
def unir_pdfs(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()  # Crea un objeto PdfMerger

    # Itera sobre los documentos recibidos y los agrega al objeto PdfMerger
    for document in documents:
        pdf_final.append(document)
    
    # Escribe el PDF final en el archivo de salida
    pdf_final.write(output_path)

# Función para dividir un PDF en varios archivos
def dividir_pdf(input_path, output_path, start_page, end_page):
    pdf_reader = PyPDF2.PdfReader(input_path)  # Crea un objeto PdfReader para el PDF de entrada
    pdf_writer = PyPDF2.PdfWriter()  # Crea un objeto PdfWriter para escribir el PDF de salida

    # Itera sobre las páginas del PDF de entrada y las agrega al objeto PdfWriter
    for page_number in range(start_page, end_page+1):
        pdf_writer.add_page(pdf_reader.pages[page_number])
    
    # Escribe el PDF dividido en el archivo de salida
    with open(output_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

# Función para proteger un PDF con contraseña
def proteger_pdf(input_path, output_path, password):
    pdf_reader = PyPDF2.PdfReader(input_path)  # Crea un objeto PdfReader para el PDF de entrada
    pdf_writer = PyPDF2.PdfWriter()  # Crea un objeto PdfWriter para escribir el PDF protegido

    # Itera sobre las páginas del PDF de entrada y las agrega al objeto PdfWriter
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # Encripta el PDF con la contraseña proporcionada
    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
    
    # Escribe el PDF protegido en el archivo de salida
    with open(output_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

# Página para unir PDFs
def pagina_unir_pdfs():
    st.image("assets/pdf.png", width=200)  # Muestra una imagen
    st.header("Unir varios PDF's.")  # Muestra un encabezado
    st.subheader("Adjuntar los pdfs a unir.")  # Muestra un subencabezado

    # Widget para cargar múltiples archivos PDF
    pdf_adjuntos = st.file_uploader(label="pdf-merge", accept_multiple_files=True)

    # Botón para unir los PDFs
    unir = st.button(label="Unir PDF's")

    if unir:
        if len(pdf_adjuntos) <= 1:
            st.warning("Debes adjuntar más de un PDF")  # Advierte si no se adjuntan suficientes PDFs
        else:
            unir_pdfs(output_pdf, pdf_adjuntos)  # Llama a la función para unir los PDFs
            st.success("Clic aquí para descargar el PDF final")  # Muestra un mensaje de éxito
            with open(output_pdf, "rb") as file:
                pdf_data = file.read()
            st.download_button(label="Descargar el PDF final", data=pdf_data, file_name="pdf_final.pdf")  # Botón para descargar el PDF final

# Página para dividir PDFs
def pagina_dividir_pdfs():
    st.image("assets/pdf.png", width=200)  # Muestra una imagen
    st.header("Dividir archivos PDF")  # Muestra un encabezado
    st.subheader("Abrir PDF a dividir")  # Muestra un subencabezado

    # Widget para cargar un archivo PDF
    pdf_div = st.file_uploader(label="pdf-divider", accept_multiple_files=False)

    if pdf_div is not None:
        pdf_reader = PyPDF2.PdfReader(pdf_div)  # Crea un objeto PdfReader para el PDF seleccionado
        num_paginas = len(pdf_reader.pages)  # Obtiene el número de páginas del PDF
        st.write(f"El PDF seleccionado tiene {num_paginas} páginas.")  # Muestra el número de páginas del PDF seleccionado

        st.write("Dividir el PDF cada cuántas páginas:")
        # Widget para ingresar el número de páginas por división
        paginas_por_dividir = st.number_input(label="Páginas por división", min_value=1, max_value=num_paginas, value=1)
        
        stop_here = num_paginas / paginas_por_dividir
        start_page = 0
        end_page = paginas_por_dividir - 1
        dividir = st.button(label="Dividir PDF")  # Botón para dividir el PDF
        increment = 1

        if dividir:
            if pdf_div is not None:
                while stop_here>0:
                    stop_here-=1
                    dividir_pdf(pdf_div, output_pdf_dividido, start_page, end_page)  # Llama a la función para dividir el PDF
                    st.success("Clic aquí para descargar el PDF dividido")  # Muestra un mensaje de éxito
                    with open(output_pdf_dividido, "rb") as file:
                        pdf_data = file.read()
                    st.download_button(label=f"Descargar el PDF dividido {increment}", data=pdf_data, file_name="pdf_dividido.pdf")  # Botón para descargar el PDF dividido
                    increment+=1
                    start_page = end_page + 1
                    end_page += paginas_por_dividir
                    if end_page >= num_paginas:
                        end_page = num_paginas - 1
            else:
                st.warning("Por favor, adjunta un PDF para dividir")  # Advierte si no se ha adjuntado un PDF

# Página para proteger PDFs con contraseña
def pagina_proteger_pdf():
    st.image("assets/pdf.png", width=200)  # Muestra una imagen
    st.header("Proteger archivo PDF")  # Muestra un encabezado
    st.subheader("Selecciona un PDF para proteger con contraseña")  # Muestra un subencabezado

    # Widget para cargar un archivo PDF
    pdf_prot = st.file_uploader(label="pdf-protect")

    if pdf_prot is not None:
        password = st.text_input(label="Introduce la contraseña", type="password")  # Widget para ingresar la contraseña
        confirm_password = st.text_input(label="Confirma la contraseña", type="password")  # Widget para confirmar la contraseña
        
        if password == confirm_password and password != "":
            proteger = st.button(label="Proteger PDF")  # Botón para proteger el PDF
            
            if proteger:
                proteger_pdf(pdf_prot, output_pdf_protected, password)  # Llama a la función para proteger el PDF
                st.success("Clic aquí para descargar el PDF protegido")  # Muestra un mensaje de éxito
                with open(output_pdf_protected, "rb") as file:
                    pdf_data = file.read()
                st.download_button(label="Descargar el PDF protegido", data=pdf_data, file_name="pdf_protected.pdf")  # Botón para descargar el PDF protegido
        elif password != confirm_password and confirm_password != "":
            st.error("Las contraseñas no coinciden")  # Muestra un mensaje de error si las contraseñas no coinciden

# Configuración de la barra lateral
st.sidebar.title("Menú")  # Título de la barra lateral
pagina_actual = st.sidebar.radio("Selecciona una opción", ["Unir PDFs", "Dividir PDFs", "Proteger PDF"])  # Widget de selección de página

# Mostrar la página seleccionada
if pagina_actual == "Unir PDFs":
    pagina_unir_pdfs()  # Muestra la página para unir PDFs
elif pagina_actual == "Dividir PDFs":
    pagina_dividir_pdfs()  # Muestra la página para dividir PDFs
elif pagina_actual == "Proteger PDF":
    pagina_proteger_pdf()  # Muestra la página para proteger PDFs
