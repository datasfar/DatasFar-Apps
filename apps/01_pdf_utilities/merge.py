import PyPDF2
import PyPDF2.errors
import streamlit as st

class Merge:

    def __init__(self):
        """
        Inicializa la clase Merge.
        
        Crea un objeto Merge con el nombre del archivo de salida por defecto "pdf_final.pdf".
        """

        self.output_pdf = "pdf_final.pdf"



    def merge_pdfs(self, documents):
        """
        Une varios archivos PDF en uno solo.

        Parameters:
        -----------
        documents : list
            Lista de archivos PDF a unir.

        Returns:
        --------
        None
        """

        pdf_merged = PyPDF2.PdfMerger()

        for document in documents:
            pdf_merged.append(document)
        
        pdf_merged.write(self.output_pdf)



    def merge_interface(self):
        """
        Interfaz para unir varios archivos PDF.

        Permite al usuario cargar múltiples archivos PDF y fusionarlos en un único archivo.
        """
        
        left_co, cent_co,last_co = st.columns(3)

        with cent_co:
            st.image("assets/merge.png", width=200)

        st.header("Unir varios PDF's.")
        st.subheader("Adjuntar los pdfs a unir.")

        attached_files = st.file_uploader(label="Unir PDFs", accept_multiple_files=True)

        merge_action = st.button(label="Unir PDF's")

        if merge_action:
            if len(attached_files) <= 1:

                st.warning("Debes adjuntar más de un documento.")

            else:

                try:
                    self.merge_pdfs(attached_files)
                    st.success("Documentos unidos correctamente.")

                    with open(self.output_pdf, "rb") as file:
                        pdf_merged = file.read()

                    st.download_button(label="Descargar el documento", data=pdf_merged, file_name="pdf_final.pdf")

                except PyPDF2.errors.PdfReadError:
                    st.error("Uno o más archivos adjuntados no son PDFs válidos.")