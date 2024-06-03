import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles
import apps_library.constants as constants

from apps_library.components.navbar import navbar
from apps_library.components.app_description import app_description
from apps_library.components.images_show import images_show

@rx.page(
    route=Route.PDF_UTILS.value,
    title=utils.pdf_utils_title,
    description=utils.pdf_utils_description,
    image=utils.preview,
    meta=utils.pdf_utils_meta
)
def pdf_utils() -> rx.Component:
    return rx.box(
        utils.lang(),
        rx.vstack(
            navbar(),
            app_description("/pdf.png", "PDF Utils", "La aplicación permite: unir, dividir y proteger con contraseña documentos pdf. Utilizando la librería PyPDF.", constants.PDF_REPO),
            rx.markdown('''### FUNCIONALIDADES:
    1. Unir varios documentos PDF en uno.
    2. Separar un documento PDF en varios.
    3. Proteger un documento PDF con contraseña.

### DEPENDENCIAS:
    - PyPDF2
    - streamlit
            '''),
            images_show(["/pdf_utils_image/1.png", "/pdf_utils_image/2.png", "/pdf_utils_image/3.png", "/pdf_utils_image/4.png", "/pdf_utils_image/5.png"]),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )