import reflex as rx
from .. import styles
from ..components.sidebar import sidebar
from ..components.speed_dial import render_speed_dial

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]

def custom_template(page_content: rx.Component) -> rx.Component:
    """Template personalizado que incluye sidebar y speed dial.
    
    Args:
        page_content: El contenido de la página que se renderizará en el área principal
    """
    return rx.flex(
        rx.flex(
            sidebar(),
            rx.vstack(
                rx.box(
                    rx.heading(
                        "Bienvenido, usuario",
                        as_="h1",
                        size="5",
                        padding="1em"
                    ),
                    width="100%",
                ),
                rx.box(
                    page_content,
                    padding="1.5em",
                    position="relative",
                    height="100dvh",
                    width="100%",
                    
                    id="main-content",
                ),
                width="100%",
                spacing="0",
            ),
            flex_direction=["column", "column", "column", "row"],
            max_height="100dvh",
            width="100%",
        ),
        render_speed_dial(),  # Ensure speed dial is rendered on top
    )

# Función helper para crear páginas usando el template
def create_page(route: str, title: str):
    """Decorador para crear páginas usando el template personalizado.
    
    Args:
        route: La ruta de la página
        title: El título de la página
    """
    def decorator(page_content: callable):
        @rx.page(route=route, title=title)
        def wrapped_page():
            return custom_template(page_content())
        return wrapped_page
    return decorator