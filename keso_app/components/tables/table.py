import reflex as rx
from typing import List, Any

table_style = {
    
}

table_config = {
    
}

# Display control

def create_header(header: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            # rx.icon(icon, size=18),
            rx.text(header),
            align="center",
            spacing="2",
        )
    )

def display_headers(headers: List[str]) -> rx.Component:
    return rx.table.header(
        rx.table.row(
            rx.foreach(
                headers,
                create_header
            ),
        ),
    ),

def create_cell(cell_value: Any) -> rx.Component:
    return rx.table.cell(cell_value)  

def create_row(row_dict) -> rx.Component:
    return rx.table.row(
        rx.foreach(
            row_dict.values(),
            create_cell
        )
    )

def display_body(rows: List[dict]) -> rx.Component:
    return rx.table.body(
        rx.foreach(
            rows,
            create_row
        ),
    ),

# Visual components

def sort_controls() -> rx.Component:
    return rx.text("Sort controls")

def search_filter() -> rx.Component:
    return rx.text("Search filter")

def export_button() -> rx.Component:
    return rx.text("Export button")

def main_filter() -> rx.Component:
    return rx.text("Main filter")

def _pagination_controls(data_state: rx.state) -> rx.Component:
    return rx.hstack(
        rx.button(
            "Previous",
            on_click=data_state.prev_page,
        ),
        rx.text(
            f"Page {data_state.page_number} of {data_state.total_pages}"
        ),
        rx.button(
            "Next",
            on_click=data_state.next_page,
        ),
        spacing="4",
    )

def table_component(data_state: rx.state) -> rx.Component:
    return rx.vstack(
        _pagination_controls(data_state),
        rx.table.root(
            display_headers(data_state.headers),
            display_body(data_state.current_page_data),
            variant="surface",
            on_mount=data_state.load_entries,
            width="100%",
        ),
        width="100%",
        padding="4",
    )