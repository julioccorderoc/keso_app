import reflex as rx
from ..navigation import routes
from .. import styles
from ..template.base import create_page

@create_page(route=routes.HOME_ROUTE, title="Resumen")
def home():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
    )