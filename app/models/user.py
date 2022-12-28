from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: Optional[int] = Field(default=None, example=1234567)
    principal_id: str = Field(example="951f572a-f163-474b-81cf-d0d8c18a3dce")
    first_name: str = Field(example="Johnny")
    last_name: str = Field(example="Appleseed")

    class Config:
        orm_mode = True
