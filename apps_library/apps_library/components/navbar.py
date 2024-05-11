import reflex as rx
import apps_library.styles.styles as styles

from apps_library.routes import Route

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.link(
                rx.box(
                    rx.text("Apps")
                ),
                href="/",
                style=styles.NAVBAR_LINK_STYLES
            ),
            rx.link(
                rx.box(
                    rx.text("Tutoriales")
                ),
                href=Route.TUTORIALS.value,
                style=styles.NAVBAR_LINK_STYLES
            )
        ),

        rx.link(
            rx.hstack(
                rx.icon(tag="github"),
                rx.text("Repositorio"),
            ),
            href="https://github.com/datasfar/DatasFar-Apps/tree/main/apps",
            style=styles.NAVBAR_LINK_STYLES
        ),

        style=styles.NAVBAR_STYLES
        
    )