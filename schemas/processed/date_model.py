"""
A module for date model in the schemas-processed package.
"""
from datetime import datetime
from typing import Any

from pydantic import BaseModel, field_validator


class DateModel(BaseModel):
    day: int
    month: int
    year: int

    @field_validator("day", "month", "year", mode="before", check_fields=True)
    def split_date(cls, v: Any, values: Any) -> Any:
        """
        Ensure that the given representation are valid
        :param v: The given attribute variables
        :type v: Any
        :param values: The given attribute values
        :type values: Any
        :return: The separated and validated date
        :rtype: Any
        """
        if "year" in values:
            return v
        date_obj = datetime.strptime(str(v), '%Y%m%d')
        values["day"] = date_obj.day
        values["month"] = date_obj.month
        values["year"] = date_obj.year
        return v
