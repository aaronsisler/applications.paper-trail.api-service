from pydantic import BaseModel

from ..models.mapper_type import MapperType


class CitiRawTransactionFieldTypeMapper(BaseModel):
    Status = MapperType.STRING
    Date = MapperType.STRING
    Description = MapperType.STRING
    Debit = MapperType.DECIMAL
    Credit = MapperType.DECIMAL
