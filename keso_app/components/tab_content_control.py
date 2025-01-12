import reflex as rx
from typing import List

def tab_content_control(
    tab_values: List[str],
    tab_state: rx.State
    ) -> rx.Component:
    
    triggers = [rx.tabs.trigger(value, value=value) for value in tab_values]
    
    return rx.tabs.root(
        rx.tabs.list(*triggers),
        default_value=tab_values[0] if tab_values else None,
        value=tab_state.selected_tab,
        on_change=tab_state.set_selected_tab,
    )   