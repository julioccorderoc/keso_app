import reflex as rx
from ..states import routes
from ..template.base import create_page
from ..components.tab_content_control import tab_content_control
from ..components.tables.ag_table import ag_table
from .. import styles

PRODUCTION_TABS = ["Leche", "Queso", "Suero"]
class Production_Table_State(rx.State):
    selected_tab: str = PRODUCTION_TABS[0]

    @rx.event
    def set_selected_tab(self, value: str):
        self.selected_tab = value

import json
with open(r"C:\Users\USER\Documents\CheeseFarm\keso_app\data_mockup\tables\milk_batches.json") as f:
    json_data = json.load(f)

@create_page(route=routes.PRODUCTION_ROUTE, title="Producción")
def production():

    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
        tab_content_control(PRODUCTION_TABS, Production_Table_State),
        rx.text(f"{Production_Table_State.selected_tab}  clicked !"),
        ag_table("production_table", json_data),
    )