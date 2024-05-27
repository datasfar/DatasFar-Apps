import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles

from apps_library.components.navbar import navbar
from apps_library.components.app_description import app_description
from apps_library.components.images_show import images_show


@rx.page(
    route=Route.YT_DOWNLOADER.value,
    title=utils.yt_downloader_title,
    description=utils.yt_downloader_description,
)
def yt_downloader() -> rx.Component:
    return rx.box(
        utils.lang(),
        rx.vstack(
            navbar(),
            app_description("/youtube.png", "Youtube Downloader", "Permite descargar videos de youtube, o solo el audio. Cuenta con una preview del video a descargar."),
            images_show([
                "/yt_downloader/0.png", 
                "/yt_downloader/1.png", 
                "/yt_downloader/2.png"]),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )