from typing import Union, List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.routers import institutions_router
from data_access_layer.database import SessionLocal
from dtos.user_dto import UserDto
from models.user import User

app = FastAPI()

app.include_router(institutions_router.router)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/health")
def get_application_health():
    return {"status": "UP"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/users/", response_model=List[User])
def show_records(db: Session = Depends(get_db)):
    records = db.query(UserDto).all()
    return records
