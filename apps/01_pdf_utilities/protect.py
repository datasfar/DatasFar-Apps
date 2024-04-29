import PyPDF2.errors
import streamlit as st
import PyPDF2

class Protect():

    def __init__(self) -> None:
        """
        Inicializa la clase PDFProtector.

        Crea un objeto PDFProtector con el nombre del archivo de salida por defecto "pdf_protegido.pdf".
        """
        
        self.output_pdf = "pdf_protegido.pdf" 



    def protect_pdf(self, document, password):
        """
        Protege un archivo PDF con una contraseña.

        Parameters:
        -----------
        document : BytesIO
            Archivo PDF a proteger.
        password : str
            Contraseña para proteger el archivo PDF.

        Returns:
        --------
        None
        """

        try:
            pdf_reader = PyPDF2.PdfReader(document)
            pdf_writer = PyPDF2.PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            pdf_writer.encrypt(user_password=password, owner_pwd=None, use_128bit=True)

            with open(self.output_pdf, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

        except PyPDF2.errors.PdfReadError:
            raise ValueError("El archivo adjuntado no es un PDF válido.")



    def protect_interface(self):
        """
        Interfaz para proteger un archivo PDF.

        Permite al usuario cargar un archivo PDF y protegerlo con una contraseña.
        """

        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image("assets/secure.png", width=200)
        st.header("Proteger archivo PDF")
        st.subheader("Adjunta el documento a proteger")

        attached_file = st.file_uploader(label="Proteger PDF")

        if attached_file is not None:

            password = st.text_input(label="Introduce la contraseña", type="password")
            confirm_password = st.text_input(label="Confirma la contraseña", type="password")
            protect_action = st.button(label="Proteger PDF")

            if password == confirm_password and password != "":

                if protect_action:
                    try:
                        self.protect_pdf(attached_file, password)

                        st.success("Documento protegido correctamente.")

                        with open(self.output_pdf, "rb") as file:
                            pdf_data = file.read()

                        st.download_button(label="Descargar el PDF protegido", data=pdf_data, file_name="pdf_final.pdf")
                    
                    except Exception as e:
                        st.error(f"Se produjo un error al proteger el PDF. {e}")


            elif password != confirm_password and confirm_password != "":
                st.error("Las contraseñas no coinciden")