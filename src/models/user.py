from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: Optional[int] = None
    principal_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
