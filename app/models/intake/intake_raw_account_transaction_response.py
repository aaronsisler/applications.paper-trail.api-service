from pydantic import BaseModel


class IntakeRawAccountTransactionResponse(BaseModel):
    request_id: str
    receipt_id: str
