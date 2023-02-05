from sqlalchemy import Column, Integer, String

from ..dtos.base import Base


class UserDto(Base):
    user_id = Column(Integer, primary_key=True, index=True)
    principal_id = Column(String(255), index=True)
    last_name = Column(String(255))
    first_name = Column(String(255))
