import reflex as rx

def image(image:str) -> rx.Component:
    return rx.image(
        src=image,
        width="250px",
        height="450px",
        border_radius="15px"
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
    



 