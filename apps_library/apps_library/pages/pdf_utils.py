import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.app_description import app_description
from apps_library.components.images_show import images_show
from apps_library.components.card import card
from apps_library.components.app_card import app_card

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
            app_description(),
            images_show(["/pdf_utils_image/1.png", "/pdf_utils_image/2.png", "/pdf_utils_image/3.png", "/pdf_utils_image/4.png", "/pdf_utils_image/5.png"]),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )