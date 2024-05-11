import reflex as rx

def app_description() -> rx.Component:
    return rx.hstack(
            rx.hstack(
                rx.box(
                    rx.image(
                        src="/pdf.png",
                        filter = "grayscale(100%) invert(100%)",
                        width="120px",
                        height="120px"
                    ), 
                background_color="#3faa7a",
                padding="1em",
                border_radius="15px",
                margin_right="1em"
                ), 
                rx.vstack(
                    rx.heading("PDF Utils"),
                    rx.text(
                        "Lorem ipsum dolor siet amet dor migo lomayd sdoj. Opsum dolor siet amet dor migo lomayd sdoj.",
                        max_width="300px"
                    ),
                ),
            ),
            rx.vstack(
                rx.button(
                    rx.icon(tag="download"),
                    "Descargar",
                    width="100%",
                    background_color="#3faa7a"
                ),
                rx.button(
                    rx.icon(tag="code"),
                    "Ver Código",
                    width="100%",
                    background_color="#3faa7a"
                ),
                rx.button(
                    rx.icon(tag="panels-top-left"),
                    "Live Demo",
                    width="100%",
                    background_color="#3faa7a"
                ),
                padding_x="2em"
            ),
        width="100%",
        margin_bottom="1em",
        align_items="center",
        justify_content="space-between" 
    )
    