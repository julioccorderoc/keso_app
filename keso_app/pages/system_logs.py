import reflex as rx
from ..states import routes
from .. import styles
from ..template.base import create_page

@create_page(route=routes.SYSTEM_LOGS_ROUTE, title="Registros")
def system_logs():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
    )