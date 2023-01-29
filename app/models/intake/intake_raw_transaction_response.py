from pydantic import BaseModel


class IntakeRawTransactionResponse(BaseModel):
    request_id: str
    receipt_id: str
