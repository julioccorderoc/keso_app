import reflex as rx
from typing import Callable # TODO: add proper annotation

from keso_app.constants.shared import PAGE_SIZE_OPTIONS

# TODO: disable and enable based on the number of available entries and LOADING


def _select_page_size(data_state) -> rx.Component:
    return rx.flex(
        rx.text("Rows per page: "),
        rx.select.root(
            rx.select.trigger(radius = "full", variant = "soft"),
            rx.select.content(
                rx.select.group(
                    rx.foreach(
                        PAGE_SIZE_OPTIONS,
                        lambda option: rx.select.item(option[0], value = option[1])
                    )
                ),
            ),
            value = data_state.items_per_page.to_string(),
            on_change = data_state.set_items_per_page,
            disabled = False,
        ),
        spacing = "2",
    )

def _button_pagination(icon: str, on_click_action: Callable, is_disabled: bool) -> rx.Component:
    return rx.button(
        rx.icon(icon),
        radius = "full",
        variant = "outline",
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
        _select_page_size(data_state),
        _pagination_status(data_state),
        rx.hstack(
            _button_pagination(
                icon = "chevrons-left",
                on_click_action = data_state.go_to_first_page,
                is_disabled = (data_state.current_page <= 1)
            ),
            _button_pagination(
                icon = "chevron-left",
                on_click_action = data_state.go_to_prev_page,
                is_disabled = (data_state.current_page <= 1)
            ),
            _button_pagination(
                icon = "chevron-right",
                on_click_action = data_state.go_to_next_page,
                is_disabled = (data_state.current_page >= data_state.total_pages)
            ),
            _button_pagination(
                icon = "chevrons-right",
                on_click_action = data_state.go_to_last_page,
                is_disabled = (data_state.current_page >= data_state.total_pages)
            ),
            spacing = "2",
        ),
        # direction=["column", "row"], # TODO: make it responsive
        justify = "between",
        align = "center",
        width = "100%",
    )