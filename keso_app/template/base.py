import reflex as rx
from .. import styles
from ..components.navigation_menu import nav_menu
from ..components.speed_dial import render_speed_dial

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]

def welcome_header() -> rx.Component:
    return rx.heading(
        "Bienvenido, usuario",
        as_="h2",
        size="5",
        padding="1em",
        width="100%",
        id="welcome_header"
    )

def custom_template(page_content: rx.Component) -> rx.Component:
    return rx.flex(
        nav_menu(),
        rx.flex(
            rx.vstack(
                welcome_header(),
                rx.box( # without this box, the content will be shrinked to the left
                    page_content,
                    width="100%",
                    **styles.template_content_style,
                    id="base_main_content",
                ),
                width="100%",
                id="stack_header_content",
            ),
            width="100%",
            **styles.template_page_style,
            max_width=[
                "100%",
                "100%",
                "100%",
                "100%",
                "100%",
                styles.max_width,
            ],
        ),
        render_speed_dial(),
        # flex_direction=[ # this make the sidebar to be on top of the content for most sizes, YES, this is because the working sidebar works with row and change to navbar when is colum, however, this doesn't explain why the sidebar is stuck at the top of the page
        #     "column",
        #     "column",
        #     "column",
        #     "column",
        #     "column",
        #     "row",
        # ],
        width="100%",
        margin="auto",
        position="relative",
        #max_height="100dvh",
        id="base_template",
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