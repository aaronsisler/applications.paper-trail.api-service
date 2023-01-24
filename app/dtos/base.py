import typing as t

import humps
from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: t.Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: t.Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return humps.decamelize(cls.__name__.replace("Dto", "")).upper()
        # return cls.__name__.upper().replace("DTO", "")
