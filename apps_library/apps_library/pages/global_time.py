import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.app_description import app_description
from apps_library.components.images_show import images_show


@rx.page(
    route=Route.GLOBAL_TIME.value,
    title=utils.global_time_title,
    description=utils.global_time_description,
)
def global_time() -> rx.Component:
    return rx.box(
        utils.lang(),
        rx.vstack(
            navbar(),
            app_description("/worldtime.png", "Global Time", "Permite ver la hora correspondiente en los paises seleccionados, para una fecha concreta en un pais concreto."),
            images_show([
                "/global_time/0.png", 
                "/global_time/1.png", 
                "/global_time/2.png", 
                ]),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )