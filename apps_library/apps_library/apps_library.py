import reflex as rx

from apps_library.pages.index import index
from apps_library.pages.tutorials import tutorials
from apps_library.pages.pdf_utils import pdf_utils
from apps_library.pages.image_utils import image_utils

import apps_library.styles.styles as styles

app = rx.App(
    style=styles.MAIN_STYLES
)

app.add_page(tutorials),
app.add_page(pdf_utils),
app.add_page(image_utils)
