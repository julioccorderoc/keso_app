import reflex as rx
from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date, datetime

# Add time
# Validate why rx.Base is not working

class CheeseProductionView(BaseModel):
    """Represents the cheese production view table."""
    batch_id: int
    batch_date: date
    kilos_of_cheese: float
    liters_per_kilo: float
    salt_per_liter: float
    comments: Optional[str]
    
    @field_validator('batch_date', mode='before')
    @classmethod
    def parse_timestamp_to_date(cls, value: datetime) -> date:
        """
        Accepts various inputs (str, datetime) and extracts the date part.
        Handles potential parsing errors.
        """
        if isinstance(value, datetime):
            return value.date()
        if isinstance(value, date):
            return value
        if isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
                return dt.date()
            except ValueError:
                raise ValueError(f"Invalid date/timestamp format: {value}")
        raise TypeError(f"Unexpected type for date parsing: {type(value)}")