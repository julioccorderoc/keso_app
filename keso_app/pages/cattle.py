import reflex as rx
from ..navigation import routes
from .. import styles
from ..template.base import create_page

@create_page(route=routes.CATTLE_ROUTE, title="Ganado")
def cattle():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
    )