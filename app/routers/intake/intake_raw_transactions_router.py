import uuid
from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import deps
from app.models.intake.intake_raw_transaction_request import IntakeRawTransactionRequest
from app.models.intake.intake_raw_transaction_response import IntakeRawTransactionResponse
from app.models.raw_account_transaction import RawAccountTransaction
from app.models.supported_institution import SupportedInstitution
from app.services.intake.citi_raw_account_transaction_intake_service import CitiRawAccountTransactionIntakeService
from app.utils.intake.csv_file_parser import CsvFileParser

router = APIRouter(
    prefix="/intake/raw-transactions",
    responses={404: {"description": "Not found"}},
)


@router.post("/test", status_code=200, response_model=IntakeRawTransactionResponse)
def post_intake_raw_transactions(request: IntakeRawTransactionRequest):
    return IntakeRawTransactionResponse(request_id=request.request_id, receipt_id=str(uuid.uuid4()))


@router.post("", status_code=200, response_model=Sequence[RawAccountTransaction])
def post_intake_raw_transactions(request: IntakeRawTransactionRequest, db: Session = Depends(deps.get_db)) -> list:
    try:
        generic_list = CsvFileParser.parse(request.file)

        created_trans_list = []

        match request.institution:
            case SupportedInstitution.CITI:
                created_trans_list = CitiRawAccountTransactionIntakeService.intake(generic_list, request.account_id,
                                                                                   request.user_id, db)
            case _:
                pass

        return created_trans_list
    except Exception as e:
        print("Exception", e)
        return []
