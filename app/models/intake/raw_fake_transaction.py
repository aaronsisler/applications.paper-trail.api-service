from humps import camelize
from pydantic import BaseModel, Field


def to_camel(string):
    return camelize(string)


class RawFakeTransaction(BaseModel):
    id: int = Field(example=1234567)
    amount: float = Field(example=123.45)
    first_name: str = Field(example="Johnny")
    last_name: str = Field(example="Appleseed")

    class Config:
        orm_mode = True
        alias_generator = to_camel
