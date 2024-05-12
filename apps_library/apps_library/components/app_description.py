import reflex as rx
import apps_library.styles.styles as styles


def app_description(image:str, title:str, description:str) -> rx.Component:
    return rx.hstack(
            rx.hstack(
                rx.box(
                    rx.image(
                        src=image,
                        style=styles.SHOW_APP_IMAGE
                    ), 
                style=styles.SHOW_APP_IMAGE_BOX
                ), 
                rx.vstack(
                    rx.heading(title),
                    rx.text(
                        description,
                        max_width="300px"
                    ),
                ),
            ),
            rx.vstack(
                rx.button(
                    rx.icon(tag="download"),
                    "Descargar",
                    style=styles.SHOW_APP_BUTTONS
                ),
                rx.button(
                    rx.icon(tag="code"),
                    "Ver Código",
                    style=styles.SHOW_APP_BUTTONS
                ),
                rx.button(
                    rx.icon(tag="panels-top-left"),
                    "Live Demo",
                    style=styles.SHOW_APP_BUTTONS
                ),
                style=styles.SHOW_APP_BUTTONS_BOX
            ),
        style=styles.APP_DESCRIPTION_MAIN
    )
    