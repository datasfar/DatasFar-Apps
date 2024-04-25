import reflex as rx

import apps_library.styles.styles as styles
def card(title:str, description:str, image:str) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                title,
                style=styles.CARD_TITLE_STYLES
            ),
            rx.text(
                description,
                style=styles.CARD_DESCRIPTION_STYLES
            ),
            style=styles.CARD_INFO_STYLES
        ),
        rx.box(
            rx.image(
                src=image,
                style=styles.CARD_IMAGE_STYLES
            ),
            width="40%",
            overflow="hidden",
            border_radius="15px"
        ),
        style=styles.CARD_STYLES
    )