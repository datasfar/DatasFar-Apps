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