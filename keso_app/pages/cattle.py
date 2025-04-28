import reflex as rx
from ..template.base import create_page
from ..states import cheese_state, routes
from ..components.table.table import table_component
from ..components.table.pagination import pagination
from ..components.table.controls import table_controls
from .. import styles

def data_display(data_state) -> rx.Component:
    return rx.vstack(
        table_controls(data_state),
        table_component(data_state),
        pagination(data_state),
        width="100%",
        padding="4",
    )


@create_page(route=routes.CATTLE_ROUTE, title="Ganado")
def cattle():
    return rx.vstack(
        data_display(cheese_state.CheeseState),
        width="100%",
    )