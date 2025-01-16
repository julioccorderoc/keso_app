import reflex as rx
from typing import Optional

form_config = {}

form_style = {}

# TODO pass kwargs to the form controls instead of predefined parameters

def _form_control_input(
        name: str,
        required: bool,
        placeholder: str = "",
        type: str = "text",
        default_value: str = "",
        item_list: list = [],
    ) -> rx.Component:
    
    return rx.input(
        name=name,
        required=required,
        placeholder=placeholder, 
        type=type, 
        default_value=default_value,
        high_contrast=True,
        width="100%",
        as_child=True,
    ),

def _form_control_select(
        name: str,
        required: bool,
        placeholder: str = "",
        type: str = "text",
        default_value: str = "",
        item_list: list = []
    ) -> rx.Component:
    
    return rx.select(
        name=name,
        required=required,
        items=item_list,
        placeholder=placeholder,
        high_contrast=True,
        direction="row",
        width="100%",
        as_child=True,
    ),

def _form_control_textarea(
        name: str,
        required: bool,
        placeholder: str = "",
        type: str = "text",
        default_value: str = "",
        item_list: list = [],
    ) -> rx.Component:
    
    return rx.text_area(
        name=name,
        required=required,
        placeholder=placeholder,
        default_value=default_value,
        high_contrast=True,
        max_length=140,
        rows="2",
        resize="vertical",
        width="100%",
        as_child=True,
    ),


def _form_field_control(
        field_type: str,
        **kwargs,
    ) -> rx.Component:
    
    return rx.match(
        field_type,
        ("select", rx.fragment(_form_control_select(**kwargs))),
        ("textarea", rx.fragment(_form_control_textarea(**kwargs))),
        ("input", rx.fragment(_form_control_input(**kwargs))),
        rx.text(f"Unknown field type: {field_type}")
    ),


def _form_field_label(
        icon_tag: str,
        label: str,
    ) -> rx.Component:

    return rx.hstack(
        rx.icon(
            icon_tag, 
            size=16,
            stroke_width=1.5
        ),
        rx.text(label),
        align="center",
        spacing="2",
    )

def _form_field(
        field_type: str,
        icon_tag: str,
        label: str,
        **kwargs,
    ) -> rx.Component:

    return rx.vstack(
        _form_field_label(icon_tag, label),
        _form_field_control(field_type=field_type, **kwargs),
        direction="column",
        width="100%",
        spacing="3",
    )


def add_milk_batch_form() -> rx.Component:
    
    return rx.flex(
        rx.hstack(
            # cow from where the milk is being produced
            _form_field(
                field_type="select",
                icon_tag="paw-print",
                label="Vaca",
                name="cow_code",
                required=True,
                placeholder="Selecciona una vaca",
                type="text",
                default_value="",
                item_list=["CO001", "CO002", "CO003"],
            ),
            # milk produced
            _form_field(
                field_type="input",
                icon_tag="milk",
                label="Lecha extraida",
                name="milk_produced",
                required=True,
                placeholder="Litros producidos",
                type="number",
                default_value=""
            ),
            spacing="3",
            width="100%",
        ),
        # comments and observations
        _form_field(
            field_type="textarea",
            icon_tag="message-square-text",
            label="Observaciones",
            name="comments",
            required=False,
            placeholder="Escribe tus observaciones aqui...",
            type="text",
            default_value="",
        ),
        direction="column",
        spacing="5",
    )

def add_cheese_batch_form() -> rx.Component:
    return rx.form()

def add_expense_form() -> rx.Component:
    return rx.form()

def add_revenue_form() -> rx.Component:
    return rx.form()

def add_expense_form() -> rx.Component:
    return rx.form()

def add_transaction_form() -> rx.Component:
    return rx.form()

def add_cow_birth_form() -> rx.Component:
    return rx.form()

def add_cow_purchase_form() -> rx.Component:
    return rx.form()

def add_cow_death_form() -> rx.Component:
    return rx.form()

def add_item_to_inventory_form() -> rx.Component:
    return rx.form()