import reflex as rx

class Dialogs_State(rx.State):
    milk_batch_is_open: bool = False
    cheese_batch_is_open: bool = False
    revenue_is_open: bool = False
    expense_is_open: bool = False
    transaction_is_open: bool = False
    cow_birth_is_open: bool = False
    cow_purchase_is_open: bool = False
    cow_death_is_open: bool = False
    item_to_inventory_is_open: bool = False