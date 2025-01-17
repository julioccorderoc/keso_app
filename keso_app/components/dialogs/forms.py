import reflex as rx

from .add_records import dialog_form
from .forms_root import (
    add_milk_batch_form,
    add_cheese_batch_form,
    add_expense_form,
    add_revenue_form,
    add_transaction_form,
    add_cow_birth_form,
    add_cow_purchase_form,
    add_cow_death_form,
    add_item_to_inventory_form
)
from ...states import (
    Milk_Batches_DB,
    Dialogs_State
)



def dialog_form_milk_batch() -> rx.Component:

    header_config = {
        "icon": "milk",
        "title": "Nuevo lote de leche",
        "description": "Ingresa los datos de este lote de leche", 
    }
    
    return dialog_form(
        header_config,
        add_milk_batch_form,
        Milk_Batches_DB.handle_submit(),
        True,
        "milk_batch_is_open"
    )

