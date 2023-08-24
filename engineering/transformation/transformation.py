"""
A module for transformation in the engineering-transformation package.
"""
import logging
from collections import namedtuple
from typing import Any, Type

from pandas import DataFrame

from core.persistence_manager import CSVManager, DataType
from schemas.processed.bank import Bank
from schemas.processed.channel import Channel
from schemas.processed.date_model import DateModel
from schemas.processed.point_of_sale import PointOfSale
from schemas.processed.product import Product
from schemas.processed.transaction import Transaction

logger: logging.Logger = logging.getLogger(__name__)
Models: Type['Models'] = namedtuple(
    'Models',
    ['DateModel', 'PointOfSale', 'Transaction', 'Product', 'Bank', 'Channel'],
)


class DataTransformer:
    """
    Data transformation class
    """

    def __init__(self, csv_manager: CSVManager):
        self.csv_manager: CSVManager = csv_manager

    @staticmethod
    def _date_transform(df: DataFrame) -> list[DateModel]:
        dates: list[str] = df["fecha"].unique().tolist()
        return [
            DateModel(
                year=int(str(date)[:4]),
                month=int(str(date)[4:6]),
                day=int(str(date)[6:]),
            )
            for date in dates
        ]

    @staticmethod
    def _pos_transform(df: DataFrame) -> list[PointOfSale]:
        df = (
            df[["pdv", "idregion", "idciudad", "canal", "actividad"]]
            .drop_duplicates()
            .copy()
        )
        return [PointOfSale(**row.to_dict()) for _, row in df.iterrows()]

    @staticmethod
    def _transaction_transform(df: DataFrame) -> list[Transaction]:
        return [Transaction(**row.to_dict()) for _, row in df.iterrows()]

    @staticmethod
    def _product_transform(df: DataFrame) -> list[Product]:
        df = df[["producto"]].drop_duplicates().copy()
        return [
            Product(id=i, name=row["producto"])
            for i, row in enumerate(df.iterrows(), start=1)
        ]

    @staticmethod
    def _bank_transform(df: DataFrame) -> list[Bank]:
        df = df[["banco"]].drop_duplicates().copy()
        return [
            Bank(id=i, name=row["banco"])
            for i, row in enumerate(df.iterrows(), start=1)
        ]

    @staticmethod
    def _channel_transform(df: DataFrame) -> list[Channel]:
        df = df[["canal"]].drop_duplicates().copy()
        return [
            Channel(id=i, name=row["canal"])
            for i, row in enumerate(df.iterrows(), start=1)
        ]

    def transform(self) -> Models:
        """
        Transform the raw dataframes into lists of model objects
        :return: A tuple of lists of model instances
        :rtype: Models
        """
        raw_data1: DataFrame = self.csv_manager.load(
            filename="data1.txt", data_type=DataType.RAW
        )
        raw_data2: DataFrame = self.csv_manager.load(
            filename="data2.txt", data_type=DataType.RAW
        )
        raw_data3: DataFrame = self.csv_manager.load(
            filename="data3.txt", data_type=DataType.RAW
        )
        transformations_mapping: dict[str, Any] = {
            "DateModel": (self._date_transform, raw_data1),
            "PointOfSale": (self._pos_transform, raw_data3),
            "Transaction": (self._transaction_transform, raw_data2),
            "Product": (self._product_transform, raw_data2),
            "Bank": (self._bank_transform, raw_data1),
            "Channel": (self._channel_transform, raw_data3),
        }
        transformations = {
            model_name: method(df)
            for model_name, (method, df) in transformations_mapping.items()
        }
        return Models(**transformations)

    @staticmethod
    def models_to_dataframes(models: Models) -> dict[str, DataFrame]:
        """
        Convert lists of Pydantic models into Pandas DataFrames.
        :param models: The list of Pydantic models to convert
        :type models: Models
        :return: A dictionary where the key is the model name and the
         value is the DataFrame.
        :rtype: dict[str, DataFrame]
        """
        return {
            name: DataFrame([model.model_dump() for model in model_list])
            for name, model_list in models._asdict().items()
        }
