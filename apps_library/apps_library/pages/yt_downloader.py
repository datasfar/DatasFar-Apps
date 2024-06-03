import reflex as rx

from apps_library.routes import Route
import apps_library.utils as utils
import apps_library.styles.styles as styles
import apps_library.constants as constants

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
            app_description("/youtube.png", "Youtube Downloader", "Permite descargar videos de youtube, o solo el audio. Cuenta con una preview del video a descargar.", constants.YT_REPO),
            rx.markdown('''# FUNCIONALIDADES:
    1. Descarga videos de youtube, permite descargar solo audio.

# DEPENDENCIAS:
    - pytube
    - streamlit

## ERRORS:

    SSL ERROR
    Go to your applications folder and look for Python folder. Mine says "Python 3.11"
    Open that directory, there is a file called "Install Certificates.command".
    Open that file and it will run the command.

    Problema con resolución, no permite bajar a mas de 720p (limitación de pytube)
    -> descargar highest resolution only
            '''),
            images_show([
                "/yt_downloader/0.png", 
                "/yt_downloader/1.png", 
                "/yt_downloader/2.png"]),
            style=styles.CONTENT_STYLES
        ),
        style=styles.MAIN_STYLES
    )