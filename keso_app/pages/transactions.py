import reflex as rx

from ..backend import models
from ..states import routes
from .. import styles

from ..template.base import create_page
from ..components import dialog_form_milk_batch
from ..crud_pages import add_milk_batch_form, Milk_Batches_DB

trigger_button_config = {
    "button_text": "Nueva Transacción",
    "icon": "plus"
}

header_config = {
    "icon": "milk",
    "title": "Nueva Transacción",
    "description": "Este es una dialogo de prueba", 
}

action_buttons_config = {
    "on_close": rx.dialog.close(), 
    "on_submit": Milk_Batches_DB.handle_submit(),
    "submit_button_text": "Registrar leche",
    "cancel_button_text": "Cancel",
}



@create_page(route=routes.TRANSACTIONS_ROUTE, title="Transacciones")
def transactions():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
        dialog_form_milk_batch()
    )