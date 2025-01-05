import reflex as rx
from ..template.base import create_page
from ..states import table_state, routes
from ..components.tables.table import table_component
from .. import styles

@create_page(route=routes.CATTLE_ROUTE, title="Ganado")
def cattle():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
        table_component(table_state.Table_State),
        width="100%",
    )