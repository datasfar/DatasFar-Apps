import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.card import card
from apps_library.components.app_card import app_card

@rx.page(
    route=Route.TUTORIALS.value,
    title=utils.tutorials_title,
    description=utils.tutorials_description,
    image=utils.preview,
    meta=utils.tutorials_meta
)
def tutorials() -> rx.Component:
    return rx.center(
            
            rx.vstack(
                rx.heading("PROXIMAMENTE", size='9'),
                rx.link(rx.hstack(rx.icon("arrow-left"), "volver atras", color="#3faa7a"),
                        href="/",),
            ),
        style=styles.MAIN_STYLES
    )