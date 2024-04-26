import reflex as rx
import apps_library.styles.styles as styles

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
                    rx.text("Tutorials")
                ),
                href="/",
                style=styles.NAVBAR_LINK_STYLES
            )
        ),

        rx.link(
            rx.hstack(
                rx.icon(tag="github"),
                rx.text("Repositorio"),
            ),
            href="/",
            style=styles.NAVBAR_LINK_STYLES
        ),

        style=styles.NAVBAR_STYLES
        
    )