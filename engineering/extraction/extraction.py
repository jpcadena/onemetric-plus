"""
A module for extraction in the engineering-extraction package.
"""
# engineering/extraction.py
from typing import Type

import pandas as pd
from pydantic import BaseModel

from core.persistence_manager import CSVManager, DataType


def load_and_validate_data(
    filename: str, model: Type[BaseModel], data_type: DataType = DataType.RAW
) -> list[BaseModel]:
    """
        Load raw data from a given file, then validate and parse it using the
     provided pydantic model.
    :param filename: Name of the file to load
    :type filename: str
    :param model: Pydantic model for validation
    :type model: Type[BaseModel]
    :param data_type: Type of data
    :type data_type: DataType
    :return: List of parsed and validated data
    :rtype: list[BaseModel]
    """
    manager: CSVManager = CSVManager()
    dataframe: pd.DataFrame = manager.load(
        filename=filename, data_type=data_type
    )
    validated_data: list[BaseModel] = []
    for index, row in dataframe.iterrows():
        try:
            item: BaseModel = model(**row.to_dict())
            validated_data.append(item)
        except ValueError as e:
            print(f"Row {index} failed validation with error: {str(e)}")
    return validated_data
