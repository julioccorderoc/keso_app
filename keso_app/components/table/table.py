import reflex as rx
from typing import Any

from keso_app.components.table.pagination import pagination
# from keso_app.states.cheese_state import ModelType, CheeseBase

# TODO: type hints should match the state to be used, not be a generic state
# TODO: tackle the default value for pagination, currently it's 10 even if internally it's different

table_style = {
    
}

table_config = {
    
}

row_on_hover_style = {
    "_hover": {
        "background_color": "#f3f4f6",  # Tailwind's gray-100
        "transition": "background-color 150ms",
    },
    "cursor": "pointer",
    "transition": "background-color 150ms",
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

def display_headers(headers: list[str]) -> rx.Component:
    return rx.table.header(
        rx.table.row(
            rx.foreach(
                headers,
                _create_header
            ),
        ),
    ),

# Rows
def _create_cell(cell_data: tuple[str, Any]) -> rx.Component:
    _, value = cell_data
    return rx.table.cell(value)

def _get_visible_cell(column: str, row_data: dict) -> tuple[str, Any]:
    return (column, row_data[column])

def _create_row(data_state, row_data: dict) -> rx.Component:
    return rx.table.row(
        rx.foreach(
            data_state.visible_columns,
            lambda column: _create_cell(
                _get_visible_cell(
                    column, 
                    row_data
                )
            )
        )
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


# # Skeleton for loading state
# def skeleton_cell(_: rx.Var) -> rx.Component:
#     return rx.table.cell(
#         rx.skeleton(
#             rx.spinner()
#         )
#     )

# def skeleton_row(data_state) -> rx.Component:
#     return rx.table.row(
#         rx.foreach(
#             data_state.visible_columns,
#             lambda col: skeleton_cell(col)
#         )
#     )

# def display_skeleton_body(data_state) -> rx.Component:
#     return rx.foreach(
#         data_state.skeleton_range,
#         skeleton_row(data_state)
#     )


def table_component(data_state) -> rx.Component:
    return rx.vstack(
        rx.table.root(
            display_headers(data_state.visible_columns),
            display_body(data_state), # add loading logic
            variant = "surface",
            on_mount = data_state.fetch_data,
            width = "100%",
        ),
        pagination(data_state), # TODO: add a skeleton loader matching the size of pagination
        width="100%",
        padding="4",
    )