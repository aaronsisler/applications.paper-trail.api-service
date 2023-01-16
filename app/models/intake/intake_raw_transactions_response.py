from pydantic import BaseModel


class IntakeRawTransactionsResponse(BaseModel):
    request_id: str
    receipt_id: str
