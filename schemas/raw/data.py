"""
A module for data classes in the schemas-raw package.
"""
from typing import Any

from pydantic import BaseModel, field_validator


class Data1Model(BaseModel):
    pdv: str
    fecha: str
    pago: float
    cp: int
    banco: str

    @field_validator('fecha', mode="before", check_fields=True)
    def ensure_string(cls, v: str) -> str:
        """
        Ensure that the string representation is valid
        :param v: The given attribute value
        :type v: str
        :return: The string representation
        :rtype: str
        """
        return str(v)

    @field_validator('pago', mode="before", check_fields=True)
    def ensure_float(cls, v: Any) -> float:
        """
        Ensure that the given float representation is valid
        :param v: The given attribute value
        :type v: Any
        :return: The float representation
        :rtype: float
        """
        return float(v.replace(',', '.'))


class Data2Model(BaseModel):
    ventas: float
    cantidad: int
    pdv: str
    producto: str
    fecha: str
    categoria: str

    @field_validator('ventas', mode="before", check_fields=True)
    def ensure_float(cls, v: Any) -> float:
        """
        Ensure that the given float representation is valid
        :param v: The given attribute value
        :type v: Any
        :return: The float representation
        :rtype: float
        """
        return float(v.replace(',', '.'))

    @field_validator('fecha', mode="before", check_fields=True)
    def ensure_string(cls, v: str) -> str:
        """
        Ensure that the string representation is valid
        :param v: The given attribute value
        :type v: str
        :return: The string representation
        :rtype: str
        """
        return str(v)


class Data3Model(BaseModel):
    pdv: str
    idregion: int
    idciudad: int
    canal: str
    actividad: str
