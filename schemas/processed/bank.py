"""
A module for bank in the schemas-processed package.
"""
from typing import Any

from pydantic import BaseModel, field_validator


class Bank(BaseModel):
    id: int
    name: str

    @field_validator("id", mode="before", check_fields=True)
    def strip_banco(cls, v: Any) -> int:
        """
        Ensure that the given representation is valid
        :param v: The given attribute value
        :type v: Any
        :return: The int representation
        :rtype: int
        """
        return int(v.split(" ")[-1])
