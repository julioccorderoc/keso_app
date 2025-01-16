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
    
    def add_entry_to_db(self, model_class, form_data: dict):

        with rx.session() as session:
            # Crear una instancia del modelo con los datos del formulario
            new_entry = model_class(**form_data)

            # Manejar campos que no están en el formulario
            if hasattr(new_entry, "created_by_user_id"):
                new_entry.created_by_user_id = 12

            if hasattr(new_entry, "last_updated_by_user_id"):
                new_entry.last_updated_by_user_id = 12

            if hasattr(new_entry, "milk_from_cow_id"):
                new_entry.milk_from_cow_id = form_data.get("milk_from_cow_id", 12)

            session.add(new_entry)
            session.commit()

            # Opcional: Actualizar la UI si es necesario
            # yield

    def edit_entry_in_db(self, model_class, form_data: dict):
        pass
    
    def delete_entry_from_db(self, entry: Any):
        pass
    
class Milk_Batches_DB(_Data_Base):
    
    def handle_submit(
            self,
            form_data: dict
        ):
        
        form_data.pop("cow_code", None)

        # Convertir el campo milk_produced a tipo float
        if "milk_produced" in form_data:
            try:
                form_data["milk_produced"] = float(form_data["milk_produced"])
            except ValueError:
                print("Error: 'milk_produced' debe ser un número.")
                return

        return self.add_entry_to_db(Milk_Batches, form_data)
        
        
    def handle_edit(self, entry_id: int):
        pass
        
    def handle_delete(self, entry_id: int):
        pass
        
    def handle_get(self, entry_id: int):
        pass