import PyPDF2.errors
import streamlit as st
import PyPDF2

class Split():

    def __init__(self) -> None:
        """
        Inicializa la clase PDFSplitter.

        Crea un objeto PDFSplitter con el nombre del archivo de salida por defecto "pdf_dividido.pdf".
        """
        
        self.output_pdf = "pdf_dividido.pdf"


    def split_pdf(self, document, start_page, end_page):
        """
        Divide un archivo PDF en un rango de páginas dado.

        Parameters:
        -----------
        document : BytesIO
            Archivo PDF a dividir.
        start_page : int
            Página de inicio para la división del PDF.
        end_page : int
            Página final para la división del PDF.

        Returns:
        --------
        None
        """

        try:
            pdf_reader = PyPDF2.PdfReader(document)
            pdf_writer = PyPDF2.PdfWriter()

            for page_number in range(start_page, end_page+1):
                pdf_writer.add_page(pdf_reader.pages[page_number])
        
            with open(self.output_pdf, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

        except PyPDF2.errors.PdfReadError:
            raise ValueError("El archivo adjuntado no es un PDF válido.")


    def split_interface(self):
        """
        Interfaz para dividir un archivo PDF.

        Permite al usuario cargar un archivo PDF y dividirlo en varias partes.
        """

        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image("assets/split.png", width=200)
        st.header("Dividir archivos PDF")
        st.subheader("Adjuntar el documento PDF a dividir")

        attached_file = st.file_uploader(label="Dividir PDF", accept_multiple_files=False)

        if attached_file is not None:

            pdf_reader = PyPDF2.PdfReader(attached_file)

            pages_count = len(pdf_reader.pages) 
            st.write(f"El PDF seleccionado tiene {pages_count} páginas.")

            st.write("¿Cada cuantas páginas quiere dividir el documento?")
            split_indicator = st.number_input(label="Páginas por división", min_value=1, max_value=pages_count, value=1)
            split_action = st.button(label="Dividir documento")

            stopper = pages_count / split_indicator
            start_page = 0
            end_page = split_indicator -1
            increment = 1

            if split_action:
                while stopper > 0:
                    stopper -=  1
                    self.split_pdf(attached_file, start_page, end_page)
                    st.success("Documentos divididos correctamente")

                    with open(self.output_pdf, "rb") as file:
                        pdf_data = file.read()

                    st.download_button(label=f"Descargar el PDF dividido {increment}", data=pdf_data, file_name="pdf_final.pdf")
                    increment+=1

                    start_page = end_page + 1
                    end_page += split_indicator

                    if end_page >= pages_count:
                        end_page = pages_count -1

            