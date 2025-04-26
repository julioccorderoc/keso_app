import reflex as rx
from typing import Any

from keso_app.components.table.pagination import pagination

# TODO: type hints should match the state to be used, not be a generic state

table_style = {
    
}

table_config = {
    
}

# Headers
def _create_header(header: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            # rx.icon(icon, size=18),
            rx.text(header),
            align="center",
            spacing="2",
        )
    )

def display_headers(headers: set[str]) -> rx.Component:
    return rx.table.header(
        rx.table.row(
            rx.foreach(
                headers,
                _create_header
            ),
        ),
    ),

# Rows
def _create_cell(cell_value: Any) -> rx.Component:
    return rx.table.cell(cell_value)  

def _create_row(row_dict) -> rx.Component: # TODO: validate if this is a dict
    return rx.table.row(
        rx.foreach(
            row_dict.values(),
            _create_cell
        )
    )

def display_body(rows: list[dict]) -> rx.Component:
    return rx.table.body(
        rx.foreach(
            rows,
            _create_row
        ),
    ),

# Skeleton for loading state
def skeleton_cell():
    return rx.table.cell(
        rx.skeleton(
            rx.text("Loading...")
        )
    )

def skeleton_row(data_state) -> rx.Component:
    return rx.table.row(
        rx.foreach(
            data_state.headers,
            skeleton_cell
        )
    )

def display_skeleton_body(data_state) -> rx.Component:
    return rx.foreach(
        range(data_state.items_per_page),
        skeleton_row(data_state)
    )


def table_component(data_state) -> rx.Component:
    return rx.vstack(
        rx.table.root(
            display_headers(data_state.headers),
            rx.cond(
                data_state.is_loading,
                display_skeleton_body(data_state),
                display_body(data_state.current_page_data),
            ),
            variant="surface",
            on_mount=data_state.fetch_data,
            width="100%",
        ),
        pagination(data_state), # TODO: add a skeleton loader matching the size of pagination
        width="100%",
        padding="4",
    )