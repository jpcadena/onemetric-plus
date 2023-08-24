"""
A module for bank in the schemas-processed package.
"""
from pydantic import BaseModel, field_validator


class Bank(BaseModel):
    id: int
    name: str

    @field_validator("id", mode="before", check_fields=True)
    def strip_banco(cls, v):
        return int(v.split(" ")[-1])
