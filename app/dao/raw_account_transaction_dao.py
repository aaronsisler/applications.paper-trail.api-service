from typing import List, Optional, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.dtos.base import Base
from app.dtos.raw_account_tranasction_dto import RawAccountTransactionDto

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class RawAccountTransactionDao:
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, raw_account_transaction_id: int) -> Optional[RawAccountTransactionDto]:
        return db.query(self.model).filter(self.model.raw_account_transaction_id == raw_account_transaction_id).first()

    def get_all(
            self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[RawAccountTransactionDto]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


raw_account_transaction_dao = RawAccountTransactionDao(RawAccountTransactionDto)
