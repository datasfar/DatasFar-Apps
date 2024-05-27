import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.app_description import app_description
from apps_library.components.images_show import images_show


@rx.page(
    route=Route.TEXT_UTILS.value,
    title=utils.text_utils_title,
    description=utils.text_utils_description,
)
def text_utils() -> rx.Component:
    return rx.box(
        utils.lang(),
        rx.vstack(
            navbar(),
            app_description("/text.png", "Text Utils", "Permite extraer texto desde audio e imagenes, genera audios a partir de textos y convierte el formato del audio. Utiliza speech recognition y pytesseract. "),
            images_show([
                "/text_utils_image/1.png", 
                "/text_utils_image/2.png", 
                "/text_utils_image/3.png",
                "/text_utils_image/4.png", 
                "/text_utils_image/5.png", 
                "/text_utils_image/6.png"]),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )