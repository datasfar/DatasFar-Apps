import reflex as rx

import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.card import card
from apps_library.components.app_card import app_card

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
                card("Funcionando en tu propia máquina", "Podrás descargar el código y ejecutarlas en local.", "2.png"),
                card("Aprende a desarrollarlas por ti mismo", "Con nuestros video tutoriales entenderas como funcionan.", "1.png"),
                style=styles.CENTER_STYLES
            ),
            rx.heading(
                "Repositorio de apps:",
                margin_top="1.6em",
                margin_bottom="1em"
            ),
            rx.chakra.responsive_grid(
                app_card(
                    image="pdf.png",
                    name="PDF Utils",
                    description="Une, divide y protege documentos pdf.",
                    link="https://github.com/datasfar/DatasFar-Apps/tree/main/apps/01_pdf_utilities"
                ),
                app_card(
                    image="image.png",
                    name="Image Utils",
                    description="Convierte, redimensiona y elimina el fondo de una imagen.",
                    link="https://github.com/datasfar/DatasFar-Apps/tree/main/apps/02_image_utilities"
                ),
                app_card(
                    image="text.png",
                    name="Text Utils",
                    description="Extrae el texto de imagenes y audios y genera audio a partir de texto.",
                    link="https://github.com/datasfar/DatasFar-Apps/tree/main/apps/03_text_utilities"
                ),
                app_card(
                    image="pdf.png",
                    name="PDF Utils",
                    description="Une, divide y protege documentos pdf.",
                    link="https://github.com/datasfar/DatasFar-Apps/tree/main/apps/01_pdf_utilities"
                ),
                app_card(
                    image="image.png",
                    name="Image Utils",
                    description="Convierte, redimensiona y elimina el fondo de una imagen.",
                    link="https://github.com/datasfar/DatasFar-Apps/tree/main/apps/02_image_utilities"
                ),
                app_card(
                    image="text.png",
                    name="Text Utils",
                    description="Extrae el texto de imagenes y audios y genera audio a partir de texto.",
                    link="https://github.com/datasfar/DatasFar-Apps/tree/main/apps/03_text_utilities"
                ),
                width="100%",
                columns=[2, 3, 4, 4, 5],
                justify_content="space-between",
                spacing="6"
            ),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )