import reflex as rx

form_config = {}

form_style = {}

def _form_field_label(
        icon: str,
        label: str,
    ) -> rx.Component:
    
    return rx.hstack(
        rx.icon(
            icon, 
            size=16, 
            stroke_width=1.5
        ),
        rx.form.label(label),
        align="center",
        spacing="2",
    )

def _form_control_input(
        placeholder: str,
        type: str,
        required: bool,
        default_value: str = "",
    ) -> rx.Component:
    
    return rx.form.control(
        rx.input(
            placeholder=placeholder, 
            type=type, 
            default_value=default_value,
            required=required
        ),
        as_child=True,
    )
    
def _form_control_select(
        item_list: list,
        required: bool,
    ) -> rx.Component:
    
    return rx.form.control(
        rx.select(
            items=item_list,
            default_value=item_list[0],
            required=required
        ),
        as_child=True,
    )
    
def _form_control_textarea(
        placeholder: str,
        default_value: str = "",
        required: bool = False,
    ) -> rx.Component:
    
    return rx.form.control(
        rx.text_area(
            placeholder=placeholder,
            default_value=default_value,
            max_length=140,
            rows=2,
            resize="vertical",
            required=required
        ),
        as_child=True,
    )

def _form_field(
        label: str,
        placeholder: str,
        type: str,
        name: str,
        icon: str,
        default_value: str = "",
        required: bool = False,
    ) -> rx.Component:
    
    return rx.form.field(
        rx.flex(
            rx.hstack(
                rx.icon(icon, size=16, stroke_width=1.5),
                rx.form.label(label),
                align="center",
                spacing="2",
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, 
                    type=type, 
                    default_value=default_value,
                    required=required
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def add_milk_batch_form() -> rx.Component:
    
    return rx.flex(
        rx.form.root(
            rx.flex(
                # cow from where the milk is being produced
                _form_field(
                    label="Vaca",
                    placeholder="CO001",
                    type="text",
                    name="cow_code",
                    icon="icon_name",
                    default_value="CO001",
                    required=True,
                ),
                # milk produced
                _form_field(
                    label="Lecha extraida",
                    placeholder=5,
                    type="float",
                    name="milk_produced",
                    icon="icon_name",
                    default_value=5,
                    required=True,
                ),
                # comments and observations
                _form_field(
                    label="Observaciones",
                    placeholder="Escribe tus observaciones aqui...",
                    type="text",
                    name="comments",
                    icon="icon_name",
                    default_value="Produccion normal",
                    required=False,
                ),
            ),
            rx.flex(
                
            ),
        )
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