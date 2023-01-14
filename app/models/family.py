from typing import Optional, List

from pydantic import BaseModel

from app.models.user import User


class Family(BaseModel):
    family_id: Optional[int] = None
    family_name: Optional[str] = None
    family_members: Optional[List[User]] = None
