from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date, Boolean, DECIMAL

from ..dtos.base import Base


class RawAccountTransactionDto(Base):
    raw_account_transaction_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    transaction_id = Column(String(255))
    account_id = Column(String(255))
    amount = Column(DECIMAL(10, 2))
    account_transaction_date = Column(String(255))
    account_transaction_year = Column(Integer)
    account_transaction_month = Column(Integer)
    account_transaction_day = Column(Integer)
    isPending = Column(Boolean, unique=False, default=True)
    merchant_name = Column(String(255))
    merchant_name_detailed = Column(String(255))
    category_id = Column(String(255))
    category = Column(String(100))
    create_date = Column(Date)
    update_date = Column(Date)
