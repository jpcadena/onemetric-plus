"""
A module for point of sale in the schemas-processed package.
"""
from pydantic import BaseModel, field_validator


class PointOfSale(BaseModel):
    id: int
    region: int
    city: int
    channel: int
    activity: str

    @field_validator("id", mode="before", check_fields=True)
    def strip_pdv(cls, v):
        return int(v.split(" ")[1])
