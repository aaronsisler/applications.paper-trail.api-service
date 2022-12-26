from typing import Union

from fastapi import FastAPI

from src.models.supported_institution import SupportedInstitution

app = FastAPI()


@app.get("/health")
def read_root():
    return {"status": "UP"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/institutions/supported/{supported_institution}")
def get_supported_institution(supported_institution: SupportedInstitution):
    supported_institution_message_suffix = "is a supported institution!"

    match supported_institution:
        case SupportedInstitution.CITI:
            return {"supported_institution": supported_institution, "message": f"Citi {supported_institution_message_suffix}"}
        case SupportedInstitution.AMERICAN_EXPRESS:
            return {"supported_institution": supported_institution, "message": f"American Express {supported_institution_message_suffix}"}
        case _:
            # Make this an invalid type/etc. that returns a 400 based HTTP status code
            return {"institution_type": supported_institution, "message": "This is not a supported institution"}
