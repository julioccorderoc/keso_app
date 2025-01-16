import reflex as rx
from typing import List, Dict, Any, Optional
from datetime import date


import json
with open(r"/home/julioccorderoc/Cheese_Farm/keso_app/data_mockup/tables/milk_batches.json") as f:
    json_data = json.load(f)
    

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