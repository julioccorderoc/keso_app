import reflex as rx
from ..template.base import create_page
from ..states import routes
from .. import styles

import json
with open(r"C:\Users\USER\Documents\CheeseFarm\keso_app\data_mockup\tables\milk_batches.json") as f:
    json_data = json.load(f)


from typing import List, Dict, Any, Optional
from datetime import date

class milk_batches(rx.Base):
    milk_batch_id: int
    date: date
    user_id: int
    username: str
    cow_id: int
    cow_code: str
    milk: float
    comments: Optional[str] = None



class Table_State(rx.State):
    
    data: List[milk_batches] = []
    headers: List[str] = []
    total_items: int = 0
    offset: int = 0
    limit: int = 10

    # Data loading

    def load_entries(self):
        self.data = json_data
        self.headers = list(json_data[0].keys())        
        self.total_items = len(json_data)

    # Pagination control

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return (self.total_items // self.limit) + (1 if self.total_items % self.limit else 1)

    @rx.var(cache=True, initial_value=[])
    def current_page_data(self) -> List[Dict[str, Any]]:
        start = self.offset
        end = start + self.limit
        return self.data[start:end]

    def prev_page(self):
        if self.page_number > 1:
            self.offset -= self.limit

    def next_page(self):
        if self.page_number < self.total_pages:
            self.offset += self.limit
            
    def first_page(self):
        self.offset = 0

    def last_page(self):
        self.offset = (self.total_pages - 1) * self.limit



# Display control

def create_header(header: str) -> rx.Component:
    return rx.table.column_header_cell(header)

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

def create_row(row_dict: milk_batches) -> rx.Component:
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

def pagination_controls() -> rx.Component:
    return rx.hstack(
        rx.button(
            "Previous",
            on_click=Table_State.prev_page,
        ),
        rx.text(
            f"Page {Table_State.page_number} of {Table_State.total_pages}"
        ),
        rx.button(
            "Next",
            on_click=Table_State.next_page,
        ),
        spacing="4",
    )

def simple_table(data_state: rx.state) -> rx.Component:
    return rx.vstack(
        pagination_controls(),
        rx.table.root(
            # rx.table.header(
            #     rx.table.row(
            #         rx.foreach(
            #             data_state.headers,
            #             create_header
            #         ),
            #     ),
            # ),
            display_headers(data_state.headers),
            display_body(data_state.current_page_data),
            # rx.table.body(
            #     rx.foreach(
            #         data_state.current_page_data,
            #         create_row
            #     ),
            # ),
            variant="surface",
            on_mount=data_state.load_entries,
            width="100%",
        ),
        width="100%",
        padding="4",
    )

@create_page(route=routes.CATTLE_ROUTE, title="Ganado")
def cattle():
    return rx.vstack(
        rx.heading("Mi Contenido"),
        rx.text("Algo de contenido..."),
        simple_table(Table_State),
        width="100%",
    )