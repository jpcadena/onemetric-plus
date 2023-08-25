"""
A module for persistence manager in the core package.
"""
import logging
from enum import Enum
from typing import Any, Optional

import pandas as pd
from pandas.io.parsers import TextFileReader
from pydantic import PositiveInt

from core.config import InitSettings, get_init_settings

logger: logging.Logger = logging.getLogger(__name__)


class DataType(Enum):
    """
    Data Type class based on Enum
    """
    # Fixme: Rename class to PathType
    RAW: str = "data/raw/"
    PROCESSED: str = "data/processed/"
    REFERENCES: str = "references/"
    FIGURES: str = "reports/figures/"
    # Dash or Streamlit
    

class CSVManager:
    """
    CSV Persistence Manager class
    """

    def __init__(self, setting: InitSettings = get_init_settings()):
        self._encoding: str = setting.ENCODING
        self._chunk_size: PositiveInt = setting.CHUNK_SIZE

    def save(
        self,
        dataframe: pd.DataFrame,
        data_type: DataType = DataType.PROCESSED,
        filename: str = "processed_data.txt",
    ) -> bool:
        """
        Save dataframe as csv file
        :param dataframe: DataFrame to save
        :type dataframe: pd.DataFrame
        :param data_type: Path where data will be saved
        :type data_type: DataType
        :param filename: name of the file
        :type filename: str
        :return: True if the csv file was created; otherwise false
        :rtype: bool
        """
        if len(dataframe) == 0:
            return False
        if not self._encoding:
            raise AttributeError("Encoding is not set.")
        dataframe.to_csv(
            f"{data_type.value}{filename}", index=False, encoding=self._encoding
        )
        logger.info("Dataframe saved to csv")
        return True

    def load(
        self,
        filename: str = "raw_data.txt",
        data_type: DataType = DataType.RAW,
        dtypes: Optional[dict[Any, Any]] = None,
        parse_dates: Optional[list[str]] = None,
    ) -> pd.DataFrame:
        """
        Load dataframe from CSV using chunk scheme
        :param filename: name of the file including extension
        :type filename: str
        :param data_type: Path where data will be saved
        :type data_type: DataType
        :param dtypes: Data types to be used
        :type dtypes: dict
        :param parse_dates: List of date columns to parse
        :type parse_dates: list[str]
        :return: Dataframe retrieved from CSV after optimization with chunks
        :rtype: pd.DataFrame
        """
        filepath: str = f"{data_type.value}{filename}"
        if not self._encoding:
            raise AttributeError("Encoding is not set.")
        text_file_reader: TextFileReader = pd.read_csv(
            filepath,
            sep=",",
            header=0,
            chunksize=self._chunk_size,
            encoding=self._encoding,
            parse_dates=parse_dates,
        )
        dataframe: pd.DataFrame = pd.concat(text_file_reader, ignore_index=True)
        if dtypes:
            for key, value in dtypes.items():
                if value in [float, int]:
                    dataframe[key] = pd.to_numeric(
                        dataframe[key], errors="coerce"
                    )
                    dataframe[key] = dataframe[key].astype(value)
                else:
                    dataframe[key] = dataframe[key].astype(value)
        logger.info("Dataframe loaded from csv")
        return dataframe
