import reflex as rx

from keso_app.constants.shared import NO_FILTER_LABEL, NO_FILTER_VALUE

def _button_primary_action(data_state) -> rx.Component:
    return rx.button(
        rx.text("Actions"),
        radius = "large",
        variant = "solid",
        # on_click = data_state.toggle_actions
    )

def _button_sort_order(data_state) -> rx.Component:
    return rx.button(
        rx.cond(
            data_state.is_sort_ascending,
            rx.icon("arrow-down-a-z"),
            rx.icon("arrow-down-z-a"),
        ),
        radius = "large",
        variant = "ghost",
        on_click=data_state.toggle_sort_direction,
    )

def _select_sort_column(data_state) -> rx.Component:
    return rx.select.root(
        rx.select.trigger(radius = "large", variant = "surface"),
        rx.select.content(
            rx.select.group(
                rx.foreach(
                    data_state.sortable_columns,
                    lambda column: rx.select.item(column[1], value = column[0])
                )
            ),
        ),
        value = data_state.column_sorted,
        on_change = data_state.handle_sort_column,
    )

def _sort_control(data_state) -> rx.Component:
    return rx.hstack(
        _button_sort_order(data_state),
        _select_sort_column(data_state),
        spacing = "2", # FIXME: pagination not working
        align = "center",
        justify = "center",
    )

# TODO: final design will be the internal dropdown with the name and a badge with the option selected
# it'll allow to select multiple options (in that case the badge will show the number of selected options)
def _select_column_to_filter(data_state, column_to_filter) -> rx.Component:
    column_name = column_to_filter[0]
    filter_options = column_to_filter[1]
    return rx.select.root(
        rx.select.trigger(
            placeholder = column_name, 
            radius = "large", 
            variant = "soft",
            width = "100%",
        ),
        rx.select.content(
            rx.foreach(
                filter_options,
                lambda option: rx.select.item(option[0], value=option[1])
            ),
            variant = "soft",
            side = "right",
            width = "100%",
        ),
        value = data_state.active_category_filters.get(column_name, NO_FILTER_VALUE),
        on_change = lambda selected_value: data_state.handle_category_filter(column_name, selected_value),
        width = "100%",
    )

def _menu_columns_to_filter(data_state) -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                "Filters", 
                radius = "large", 
                variant = "outline"
            ),
        ),
        rx.menu.content(
            rx.foreach(
                data_state.filters_for_ui,
                lambda column: rx.menu.item(
                    _select_column_to_filter(data_state, column)
                )
            ),
            variant = "soft",
            side = "bottom",
        )
    )

def _input_search_filter(data_state) -> rx.Component:
    return rx.input(
        rx.input.slot(
            rx.icon(tag="search"),
        ),
        placeholder="Search here...",
        radius = "large",
        variant = "surface",
        on_change = data_state.handle_search_query.debounce(500),
    )

def _button_export(data_state) -> rx.Component:
    return rx.button(
        rx.icon("download"),
        radius = "large",
        variant = "surface",
        on_click = data_state.download_csv,
        disabled = False, # TODO: disable if no data is available or loading is true
    )

# TODO: render controls conditionally, depending on the data
# TODO: build this responsive
def table_controls(data_state) -> rx.Component:
    return rx.flex(
        _button_primary_action(data_state),
        rx.flex(
            _sort_control(data_state),
            _menu_columns_to_filter(data_state),
            rx.hstack(
                _input_search_filter(data_state),
                _button_export(data_state),
                spacing = "5",
                align="center",
            ),
            spacing = "5",
            align="center",
            flex_direction=["column", "row"]
        ),
        justify="between",
        align="center",
        width="100%",
        flex_direction=["column", "row"],
        spacing="5",
    )