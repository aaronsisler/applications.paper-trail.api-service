from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import deps
from app.dao.user_dao import user_dao
from app.models.user import User

router = APIRouter(
    prefix="/users",
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@router.get("/", status_code=200, response_model=Sequence[User])
def get_users(db: Session = Depends(deps.get_db)) -> dict:
    users = user_dao.get_all(db=db, limit=10)
    return users
