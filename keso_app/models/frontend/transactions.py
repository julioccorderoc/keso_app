from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date

# Transactions models for tables

class Transactions_Table(BaseModel):
    transaction_id: int
    date: date
    transaction_type: str
    description: str
    amount: Decimal
    comments: Optional[str] = None

# Transactions models for forms

class Transactions_Form(BaseModel):
    transaction_type: str
    description: str
    amount: Decimal
    comments: Optional[str] = None