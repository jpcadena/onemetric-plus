"""
A module for product in the schemas.processed package.
"""
from pydantic import BaseModel, field_validator


class Product(BaseModel):
    id: int
    name: str

    @field_validator("id", mode="before", check_fields=True)
    def strip_text(cls, v):
        return int(v.split(" ")[-1])
