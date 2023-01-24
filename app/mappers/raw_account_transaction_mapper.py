from pydantic import BaseModel

from ..models.mapper_type import MapperType


class RawAccountTransactionMapper(BaseModel):
    raw_account_transaction_id = MapperType.INTEGER
    user_id = MapperType.INTEGER
    amount = MapperType.DECIMAL
    account_transaction_date = MapperType.STRING
    account_transaction_year = MapperType.INTEGER
    account_transaction_month = MapperType.INTEGER
    account_transaction_day = MapperType.INTEGER
    is_pending = MapperType.BOOLEAN
    merchant_name = MapperType.STRING
