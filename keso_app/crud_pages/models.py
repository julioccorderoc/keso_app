from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship
import sqlalchemy
from ..utils.timing import get_utc_now
import reflex as rx


class Base_Model(rx.Model, table=False):
    
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    created_by_user_id: int = Field(default=12)
    last_updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    last_updated_by_user_id: int = Field(default=12)
    comments: Optional[str] = Field(default=None, nullable=True)

class Milk_Batches(Base_Model, table=True):

    milk_batch_id: int = Field(default=None, primary_key=True)
    milk_from_cow_id: int = Field(default=12)
    milk_produced: float = Field(nullable=False)
    
class Cheese_Batches(Base_Model, table=True):

    cheese_batch_id: int = Field(default=None, primary_key=True)
    milk_used: float = Field(nullable=False)
    salt_used: float = Field(nullable=False)
    cheese_produced: float = Field(nullable=False)
    
# class Transactions(Base_Model, table=True):

#     transaction_id: int = Field(default=None, primary_key=True)
#     transaction_type: str = Field(nullable=False)
#     description: str = Field(nullable=False)
#     amount: float = Field(nullable=False)
    
# class Inventory(Base_Model, table=True):

#     item_id: int = Field(default=None, primary_key=True)
    
# class Cows(Base_Model, table=True):

#     cow_id: int = Field(default=None, primary_key=True)
    
# class Cow_Origins(Base_Model, table=True):

#     cow_origin_id: int = Field(default=None, primary_key=True)
    
# class Cow_Births(Base_Model, table=True):

#     cow_birth_id: int = Field(default=None, primary_key=True)

# class Cow_Purchases(Base_Model, table=True):

#     cow_purchase_id: int = Field(default=None, primary_key=True)
    
# class Cow_Deaths(Base_Model, table=True):

#     cow_death_id: int = Field(default=None, primary_key=True)