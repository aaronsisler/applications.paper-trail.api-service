import uuid

from fastapi import APIRouter

from app.models.intake.intake_raw_transactions_request import IntakeRawTransactionsRequest
from app.models.intake.intake_raw_transactions_response import IntakeRawTransactionsResponse

router = APIRouter(
    prefix="/intake/raw-transactions",
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=200, response_model=IntakeRawTransactionsResponse)
def post_intake_raw_transactions(request: IntakeRawTransactionsRequest):
    return IntakeRawTransactionsResponse(request_id=request.request_id, receipt_id=str(uuid.uuid4()))
