import reflex as rx
from ..states import routes
from ..template.base import create_page
from .. import styles
from ..components.tab_content_control import tab_content_control

PRODUCTION_TABS = ["Leche", "Queso", "Suero"]
class Production_Table_State(rx.State):
    selected_tab: str = PRODUCTION_TABS[0]

    @rx.event
    def set_selected_tab(self, value: str):
        self.selected_tab = value

@create_page(route=routes.PRODUCTION_ROUTE, title="Producción")
def production():

    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
        tab_content_control(PRODUCTION_TABS, Production_Table_State),
        rx.text(f"{Production_Table_State.selected_tab}  clicked !"),
        
    )