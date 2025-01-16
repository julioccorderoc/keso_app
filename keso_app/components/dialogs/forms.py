import reflex as rx

from .add_records import dialog_form
from .forms_root import (
    add_milk_batch_form,
    add_cheese_batch_form,
    add_expense_form,
    add_transaction_form,
    add_cow_birth_form,
    add_cow_purchase_form,
    add_cow_death_form,
    add_item_to_inventory_form
)
from ...states import (
    Milk_Batches_DB
)



def dialog_form_milk_batch() -> rx.Component:
    
    trigger_button_config = {
        "button_text": "Nuevo lote de leche",
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
        "submit_button_text": "Registrar lote",
        "cancel_button_text": "Cancelar",
    }
    
    return dialog_form(
        trigger_button_config,
        header_config,
        add_milk_batch_form,
        Milk_Batches_DB.handle_submit(),
    )

