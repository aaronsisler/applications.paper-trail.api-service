from pydantic import BaseModel

from app.models.supported_institution import SupportedInstitution


class IntakeRawTransactionsRequest(BaseModel):
    request_id: str
    institution_name: SupportedInstitution
    account_owner: int
    file: str
