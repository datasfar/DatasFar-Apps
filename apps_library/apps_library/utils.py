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