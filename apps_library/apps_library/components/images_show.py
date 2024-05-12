import reflex as rx
import apps_library.styles.styles as styles

def image(image:str) -> rx.Component:
    return rx.image(
        src=image,
        style=styles.SHOW_APP_GALERY_IMAGE
    )


def images_show(images:list[str]) -> rx.Component:
    return rx.scroll_area(
        rx.hstack(
            rx.foreach(
                images,
                lambda images, index: image(
                    images
                ),
            ),
            gap=16,
        ),     
    )
    



 