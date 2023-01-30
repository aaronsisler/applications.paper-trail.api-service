from pydantic import BaseModel

from app.models.supported_institution import SupportedInstitution


class IntakeRawAccountTransactionRequest(BaseModel):
    request_id: str
    institution: SupportedInstitution
    file: str
    account_id: int
    user_id: int
