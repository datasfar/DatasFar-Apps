import reflex as rx

# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = ""

_meta = [
    
]


# Index
index_title = "Python Apps Library | By dataSfar"
index_description = "Repositorio de applicaciones utilies desarrolladas usando python y streamlit."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Tutorials
tutorials_title = "Tutoriales | By dataSfar"
tutorials_description = "Tutoriales de apps desarrolladas usando python y streamlit."

tutorials_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
tutorials_meta.extend(_meta)

# PDF Utils
pdf_utils_title = "PDF Utils | By dataSfar"
pdf_utils_description = "Aplicación de utilidades para documentos PDF."

pdf_utils_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
pdf_utils_meta.extend(_meta)

# Image Utils
image_utils_title = "Image Utils | By dataSfar"
image_utils_description = "Aplicación de utilidades para imagenes."

image_utils_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
image_utils_meta.extend(_meta)

# Text Utils
text_utils_title = "Text Utils | By dataSfar"
text_utils_description = "Aplicación de utilidades para textos."

# Youtube Downloader
yt_downloader_title = "Youtube Downloader | By dataSfar"
yt_downloader_description = "Aplicación para descargar videos de youtube."

# Global Time
global_time_title = "Global Time | By dataSfar"
global_time_description = "Aplicación de utilidades para fechas globales."
