import reflex as rx

from ..states import routes, Dialogs_State
from .. import styles

from ..template.base import create_page



def dialog_trigger_button(
        button_text: str,
        icon: str,
        dialog: str
    ) -> rx.Component:
    
    return rx.button(
            rx.icon(icon, size=26),
            rx.text(
                button_text, 
                size="4", 
                display=["none", "none", "block"]
            ),
            size="3",
            on_click=Dialogs_State.setvar(dialog, True)
        )


    



@create_page(route=routes.TRANSACTIONS_ROUTE, title="Transacciones")
def transactions():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
        dialog_trigger_button("Nuevo lote", "plus", "milk_batch_is_open")
    )