import reflex as rx
import apps_library.styles.styles as styles

def app_card(image, name, description, link) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                style=styles.APP_CARD_IMAGE
            ),
            rx.heading(name),
            rx.text(description),
            style=styles.APP_CARD_INTERN
        ),
        href=link,
        style=styles.APP_CARD_STYLE
    )