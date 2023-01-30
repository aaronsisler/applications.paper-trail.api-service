from typing import Sequence, Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import deps
from app.dao.user_dao import user_dao
from app.models.user import User

router = APIRouter(prefix="/users")


@router.get("/{user_id}", response_model=Union[User, None])
def get_user(user_id: int, db: Session = Depends(deps.get_db)) -> dict:
    return user_dao.read(db, user_id)


@router.get("", status_code=200, response_model=Sequence[User])
def get_users(db: Session = Depends(deps.get_db)) -> list:
    return user_dao.read_all(db=db, limit=10)


@router.post("", status_code=200, response_model=User)
def post_users(user: User, db: Session = Depends(deps.get_db)) -> dict:
    return user_dao.create(db=db, obj_in=user)
