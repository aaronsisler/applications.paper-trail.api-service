from pydantic import BaseModel, Field


class RawAccountTransaction(BaseModel):
    raw_account_transaction_id: int = Field(default=None, example=12345678)
    user_id: int = Field(example=2023)
    amount: float = Field(example=123.45)
    account_transaction_date: str = Field(example="2023-01-22")
    account_transaction_year: int = Field(example=2023)
    account_transaction_month: int = Field(example=1)
    account_transaction_day: int = Field(example=22)
    is_pending: bool = Field(example=True, default=False)
    merchant_name: str = Field(example="Exxon Fuel Place")

    class Config:
        orm_mode = True
