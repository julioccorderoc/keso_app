import reflex as rx
from typing import Any

# TODO: type hints should match the state to be used, not be a generic state
# TODO: skeleton before the data is loaded (the first time)

table_style = {
    
}

table_config = {
    
}

row_on_hover_style = {
    "_hover": {
        "background_color": rx.color("gray", 3),
        "transition": "background-color 150ms",
    },
    "cursor": "pointer",
    "transition": "background-color 150ms",
}

# Headers
def _create_header(header: tuple[str, str]) -> rx.Component:
    header_label = header[1]
    return rx.table.column_header_cell(
        rx.hstack(
            # rx.icon(icon, size=18),
            rx.text(header_label),
            align="center",
            spacing="2",
        )
    )

def display_headers(headers: list[tuple[str, str]]) -> rx.Component: # TODO: center headers
    return rx.table.header(
        rx.table.row(
            rx.foreach(
                headers,
                _create_header
            ),
        ),
    )

# Rows
def _create_cell(data_state, value: Any) -> rx.Component:
    return rx.table.cell(
        rx.skeleton(
            value,
            loading=data_state.is_loading,
            height="20px",
            width="100%",
        )
    )

def _get_visible_cell(column: tuple[str, str], row_data: dict) -> Any:
    field_name = column[0] # field name from the database
    return row_data[field_name]

def _create_row(data_state, row_data: dict) -> rx.Component:
    return rx.table.row(
        rx.foreach(
            data_state.visible_columns,
            lambda column: _create_cell(
                data_state,
                _get_visible_cell(
                    column, 
                    row_data
                )
            )
        ),
        style = row_on_hover_style,
        on_click = data_state.select_db_entry(row_data)
    )

def display_body(data_state) -> rx.Component:
    return rx.table.body(
        rx.foreach(
            data_state.current_page_data,
            lambda row: _create_row(
                data_state, 
                row
            )
        )
    )

def table_component(data_state) -> rx.Component:
    return rx.table.root(
        display_headers(data_state.visible_columns),
        display_body(data_state), # add loading logic
        variant = "surface",
        on_mount = data_state.fetch_data,
        width = "100%",
    )
