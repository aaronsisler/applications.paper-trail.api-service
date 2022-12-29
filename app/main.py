from typing import Sequence, Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app import deps
from app.dao.user_dao import user_dao
from app.models.user import User
from app.routers import institutions_router

app = FastAPI()

app.include_router(institutions_router.router)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/health")
def get_application_health():
    return {"status": "UP"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/users", status_code=200, response_model=Sequence[User])
def get_users(db: Session = Depends(deps.get_db)) -> dict:
    users = user_dao.get_all(db=db, limit=10)
    return users
