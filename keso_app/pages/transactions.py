import reflex as rx
from ..states import routes
from .. import styles
from ..template.base import create_page
from ..components import dialog_form
from ..crud_pages import forms



@create_page(route=routes.TRANSACTIONS_ROUTE, title="Transacciones")
def transactions():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
    )