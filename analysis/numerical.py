"""
A module for numerical in the analysis package.
"""
import pandas as pd

from core.config import InitSettings, get_init_settings


def analyze_dataframe(
    dataframe: pd.DataFrame, setting: InitSettings = get_init_settings()
) -> None:
    """
    Analyze the dataframe and its columns with inference statistics
    :param setting: The core settings dependency
    :type setting: InitSettings
    :param dataframe: DataFrame to analyze
    :type dataframe: pd.DataFrame
    :return: None
    :rtype: NoneType
    """
    print(dataframe.head())
    print(dataframe.shape)
    print(dataframe.dtypes)
    dataframe.info(memory_usage="deep")
    print(dataframe.memory_usage(deep=True))
    print(dataframe.describe(include="all", datetime_is_numeric=True))
    non_numeric_df = dataframe.select_dtypes(exclude=setting.NUMERICS)
    for column in non_numeric_df.columns:
        print(non_numeric_df[column].value_counts())
        print(non_numeric_df[column].unique())
        print(non_numeric_df[column].value_counts(normalize=True) * 100)
