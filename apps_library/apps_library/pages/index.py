import reflex as rx

import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.card import card

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        rx.vstack(
            navbar(),
            rx.hstack(
                card("Ejecuta las apps en tu propia maquina", "Podras descargar el código y ejecutar nuestras herramientas desde tu equipo.", "2.png"),
                card("Aprende a desarrollarlas por ti mismo", "Con nuestros video tutoriales entenderas como funcionan.", "1.png"),
                display="flex",
                justify_content="space-between"
            ),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )