import reflex as rx
from typing import List, Dict, Any, Optional

from ..backend.models import (
    Milk_Batches,
    Cheese_Batches,
    # Transactions,
    # Inventory,
    # Cows,
    # Cow_Origins,
    # Cow_Births,
    # Cow_Purchases,
    # Cow_Deaths,
)

class _Data_Base(rx.State):
    
    def load_entry_from_db(self):
        pass
    
    def load_entries_from_db(self):
        pass
    
    def add_entry_to_db(self, new_entry):
        with rx.session() as session:
            session.add(new_entry)
            session.commit()
            yield

    def edit_entry_in_db(self, model_class, form_data: dict):
        pass
    
    def delete_entry_from_db(self, entry: Any):
        pass
    
class Milk_Batches_DB(_Data_Base):
    
    def handle_submit(self, form_data: dict):
        
        # Handle fields that are not in the database
        form_data.pop("cow_code", None)
        
        # Create a new entry
        new_entry = Milk_Batches(**form_data)

        # Handle data that is not in the form
        if hasattr(new_entry, "created_by_user_id"):
            new_entry.created_by_user_id = 12

        if hasattr(new_entry, "last_updated_by_user_id"):
            new_entry.last_updated_by_user_id = 12

        if hasattr(new_entry, "milk_from_cow_id"):
            new_entry.milk_from_cow_id = form_data.get("milk_from_cow_id", 12)
        
        # # Convert numeric fields to float
        # if "milk_produced" in form_data:
        #     try:
        #         form_data["milk_produced"] = float(form_data["milk_produced"])
        #     except ValueError:
        #         rx.toast("Error: 'milk_produced' debe ser un número.")
        #         form_data["milk_produced"] = None

        return self.add_entry_to_db(new_entry)
        
        
    def handle_edit(self, entry_id: int):
        pass
        
    def handle_delete(self, entry_id: int):
        pass
        
    def handle_get(self, entry_id: int):
        pass