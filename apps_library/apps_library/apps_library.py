import reflex as rx

from apps_library.pages.index import index
from apps_library.pages.tutorials import tutorials
from apps_library.pages.pdf_utils import pdf_utils
from apps_library.pages.image_utils import image_utils
from apps_library.pages.text_utils import text_utils
from apps_library.pages.yt_downloader import yt_downloader
from apps_library.pages.global_time import global_time

import apps_library.styles.styles as styles

app = rx.App(
    style=styles.MAIN_STYLES
)

app.add_page(tutorials),
app.add_page(pdf_utils),
app.add_page(image_utils),
app.add_page(text_utils),
app.add_page(yt_downloader),
app.add_page(global_time)
