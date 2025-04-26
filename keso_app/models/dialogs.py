import reflex as rx
from pydantic import BaseModel
from typing import Optional
from datetime import date, time

# Validate why rx.Base is not working

class CheeseProductionEntry(BaseModel):
    """Represents a single record of cheese production."""
    batch_id: int
    batch_date: date
    batch_time: time
    kilos_of_cheese: float
    milk_used: float
    liters_per_kilo: float
    salt_used: float
    salt_per_liter: float
    comments: Optional[str]