import reflex as rx

from keso_app.constants.shared import NO_FILTER_LABEL, NO_FILTER_VALUE

def _sort_control(data_state) -> rx.Component:
    return rx.hstack(
        rx.button( # icon size 20
            rx.cond(
                data_state.is_sort_ascending,
                rx.icon("arrow-down-a-z"),
                rx.icon("arrow-down-z-a"),
            ),
            on_click=data_state.toggle_sort_direction,
        ),
        rx.select.root(
            rx.select.trigger(radius = "full", variant = "soft"),
            rx.select.content(
                # VISIBLE_COLUMNS, TODO: get from the constants
            ),
            value = "default",
            on_change = data_state.handle_sort_column,
        ),
        spacing = "2",
    )

def _search_filter(data_state) -> rx.Component:
    return rx.input(
        rx.input.slot(
            rx.icon(tag="search"),
        ),
        placeholder="Search here...",
        on_change = data_state.handle_search_query.debounce(500),
    )

def _category_filter(data_state, data_constant, column_to_filter) -> rx.Component:
    return rx.select.root(
        rx.select.trigger(placeholder=NO_FILTER_LABEL, radius = "full", variant = "soft"),
        rx.select.content(
            rx.select.group(
                *[rx.select.item(label, value=value) for label, value in data_constant.get(column_to_filter).items()]
            ),
        ),
        value = data_state.active_category_filters.get(column_to_filter, NO_FILTER_VALUE),
        on_change = lambda selected_val: data_state.handle_category_filter_change(column_to_filter, selected_val),
    ),

def _export_button(data_state) -> rx.Component:
    return rx.button(
        rx.icon("download"),
        radius = "full",
        on_click = data_state.download_csv,
        disabled = False, # TODO: disable if no data is available or loading is true
    )

# TODO: replace category filter with a filter dropdown component
def table_controls(data_state, data_constant) -> rx.Component:
    return rx.flex()