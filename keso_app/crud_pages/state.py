import reflex as rx
from typing import List, Dict, Any, Optional

class Data_Base(rx.State):
    
    data: List[Any] = []
    
    def create_entry(self, entry: Any):
        self.data.append(entry)
        
    def get_entry(self, entry_id: int):
        return self.data[entry_id]
        
    def update_entry(self, entry: Any):
        pass
        
    def delete_entry(self, entry: Any):
        self.data.remove(entry)
        



class Table_State(rx.State):
    pass