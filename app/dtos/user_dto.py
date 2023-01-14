from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date

from ..dtos.base import Base


class UserDto(Base):
    user_id = Column(Integer, primary_key=True, index=True)
    principal_id = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    first_name = Column(String(255), index=True)
    create_date = Column(Date)
    update_date = Column(Date)
