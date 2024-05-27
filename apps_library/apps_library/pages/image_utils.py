import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.app_description import app_description
from apps_library.components.images_show import images_show


@rx.page(
    route=Route.IMAGE_UTILS.value,
    title=utils.image_utils_title,
    description=utils.image_utils_description,
    image=utils.preview,
    meta=utils.image_utils_meta
)
def image_utils() -> rx.Component:
    return rx.box(
        utils.lang(),
        rx.vstack(
            navbar(),
            app_description("/image.png", "Image Utils", "Permite redimensionar y cambiar el formato de las imagenes utilizando cv2. Y elimina el fondo de una imagen con rembg."),
            images_show([
                "/image_utils_image/1.png", 
                "/image_utils_image/2.png", 
                "/image_utils_image/3.png", 
                "/image_utils_image/4.png", 
                "/image_utils_image/5.png"]),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )