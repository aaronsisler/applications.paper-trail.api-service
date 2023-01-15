from typing import Optional

from pydantic import BaseModel, Field


class RawTransaction(BaseModel):
    raw_transaction_id: Optional[int] = Field(default=None, example=1234567)
    amount: float = Field(example=123.45)
    institution_name: str = Field(example="CITI")
    account_owner: str = Field(example="Appleseed, Johnny")

    class Config:
        orm_mode = True
