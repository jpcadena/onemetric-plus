"""
A module for transaction in the schemas-processed package.
"""
from pydantic import BaseModel, field_validator

from schemas.processed.date_model import DateModel


class Transaction(BaseModel):
    sales: float
    quantity: int
    pos_id: int
    product_id: int
    date: DateModel
    category: str

    @field_validator("sales", mode="before", check_fields=True)
    def ensure_float(cls, v):
        return float(str(v).replace(',', '.'))

    @field_validator("pos_id", "product_id", mode="before", check_fields=True)
    def strip_text(cls, v):
        return int(v.split(" ")[-1])
