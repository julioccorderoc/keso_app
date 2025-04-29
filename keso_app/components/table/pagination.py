import reflex as rx
from typing import Any # TODO: remove

# TODO: disable and enable based on the number of available entries and LOADING


def _page_size_selector(data_state) -> rx.Component:
    return rx.flex(
        rx.text("Rows per page: "),
        rx.select.root(
            rx.select.trigger(radius = "full", variant = "soft"),
            rx.select.content(
                rx.select.group(
                    rx.select.item("5", value = "5", disabled = False),
                    rx.select.item("10", value = "10", disabled = False),
                    rx.select.item("25", value = "25", disabled = False),
                ),
            ),
            default_value = str(data_state.items_per_page),
            on_change = data_state.set_items_per_page,
            disabled = False,
        ),
        spacing = "2",
    )

def _pagination_button(icon: str, on_click_action: Any, is_disabled: bool) -> rx.Component:
    return rx.button(
        rx.icon(icon),
        radius = "full",
        variant = "surface",
        size = "1",
        on_click = on_click_action,
        disabled = is_disabled,
    )

def _pagination_status(data_state) -> rx.Component:
    return rx.text(
        "Page ",
        rx.code(data_state.current_page),
        f" of {data_state.total_pages}"
    )

def pagination(data_state) -> rx.Component:
    return rx.flex(
        _page_size_selector(data_state),
        _pagination_status(data_state),
        rx.hstack(
            _pagination_button(
                icon = "chevrons-left",
                on_click_action = data_state.go_to_first_page,
                is_disabled = (data_state.current_page <= 1)
            ),
            _pagination_button(
                icon = "chevron-left",
                on_click_action = data_state.go_to_prev_page,
                is_disabled = (data_state.current_page <= 1)
            ),
            _pagination_button(
                icon = "chevron-right",
                on_click_action = data_state.go_to_next_page,
                is_disabled = (data_state.current_page >= data_state.total_pages)
            ),
            _pagination_button(
                icon = "chevrons-right",
                on_click_action = data_state.go_to_last_page,
                is_disabled = (data_state.current_page >= data_state.total_pages)
            ),
            spacing = "2",
        ),
        # direction=["column", "row"], # TODO: make it responsive
        justify="between",
        align="center",
        width="100%",
    )