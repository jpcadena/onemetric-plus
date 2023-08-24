"""
A module for channel in the schemas-processed package.
"""
from pydantic import BaseModel, field_validator


class Channel(BaseModel):
    id: int
    name: str

    @field_validator("id", mode="before", check_fields=True)
    def strip_canal(cls, v):
        return int(v.split(" ")[-1])
