from enum import Enum


class MapperType(str, Enum):
    STRING = "STRING"
    DECIMAL = "DECIMAL"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
