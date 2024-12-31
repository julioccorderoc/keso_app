import reflex as rx
from ..states import routes
from .. import styles
from ..template.base import create_page

@create_page(route=routes.PRODUCTION_ROUTE, title="Producción")
def production():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
    )