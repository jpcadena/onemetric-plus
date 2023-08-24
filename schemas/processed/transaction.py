"""
A module for transaction in the schemas-processed package.
"""
from typing import Any

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
    def ensure_float(cls, v: Any) -> float:
        """
        Ensure that the given representation is valid
        :param v: The given attribute value
        :type v: Any
        :return: The float representation
        :rtype: float
        """
        return float(str(v).replace(',', '.'))

    @field_validator("pos_id", "product_id", mode="before", check_fields=True)
    def strip_text(cls, v: Any) -> int:
        """
        Ensure that the given representation are valid
        :param v: The given attribute value
        :type v: Any
        :return: The int representation
        :rtype: int
        """
        return int(v.split(" ")[-1])
