"""
A module for init settings in the app.core.config package.
"""
from functools import lru_cache

from pydantic import PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


class InitSettings(BaseSettings):
    """
    Init Settings class based on Pydantic Base Settings
    """

    model_config = SettingsConfigDict(
        case_sensitive=True,
        extra="allow",
    )

    PROJECT_NAME: str = "onemetric-plus"
    MAX_COLUMNS: PositiveInt = 50
    WIDTH: PositiveInt = 1000
    ENCODING: str = "UTF-8"
    CHUNK_SIZE: PositiveInt = 5000
    DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    DATETIME_FORMAT: str = "%d.%m.%Y"
    FILE_DATETIME_FORMAT: str = "%d-%b-%Y-%H-%M-%S"
    LOG_FORMAT: str = (
        "[%(name)s][%(asctime)s][%(levelname)s][%(module)s]"
        "[%(funcName)s][%(lineno)d]: %(message)s"
    )
    NUMERICS: list[str] = [
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "int8",
        "int16",
        "int32",
        "int64",
        "float16",
        "float32",
        "float64",
    ]
    PALETTE: str = "pastel"
    FONT_SIZE: PositiveInt = 15
    FIG_SIZE: tuple[PositiveInt, PositiveInt] = (15, 8)
    RE_PATTERN: str = "([a-z])([A-Z])"
    RE_REPL: str = r"\g<1> \g<2>"


@lru_cache()
def get_init_settings() -> InitSettings:
    """
    Get init settings cached
    :return: The init settings instance
    :rtype: InitSettings
    """
    return InitSettings()
