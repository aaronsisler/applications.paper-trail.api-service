import base64
import csv
import uuid
from typing import Sequence

import humps
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import deps
from app.dao.raw_account_transaction_dao import raw_account_transaction_dao
from app.mappers.raw_account_transaction_mapper import RawAccountTransactionMapper
from app.models.intake.intake_raw_transactions_request import IntakeRawTransactionsRequest
from app.models.intake.intake_raw_transactions_response import IntakeRawTransactionsResponse
from app.models.raw_account_transaction import RawAccountTransaction
from app.utils.csv_type_mapper import CsvTypeMapper

router = APIRouter(
    prefix="/intake/raw-transactions",
    responses={404: {"description": "Not found"}},
)


@router.post("/test", status_code=200, response_model=IntakeRawTransactionsResponse)
def post_intake_raw_transactions(request: IntakeRawTransactionsRequest):
    return IntakeRawTransactionsResponse(request_id=request.request_id, receipt_id=str(uuid.uuid4()))


@router.post("/", status_code=200, response_model=Sequence[RawAccountTransaction])
def post_intake_raw_transactions(request: IntakeRawTransactionsRequest, db: Session = Depends(deps.get_db)) -> list:
    try:
        # print(request.file)
        base64_message = request.file.replace("data:text/csv;base64,", "")

        bytes_message = base64.b64decode(base64_message)
        message_lines = str(bytes_message, "utf-8").splitlines()

        reader = csv.DictReader(message_lines, delimiter=',')

        generic_list = list(reader)
        raw_trans_list = []

        for item in generic_list:
            temp_item = CsvTypeMapper.map(vars(RawAccountTransactionMapper()), humps.decamelize(item))
            raw_account_transaction = RawAccountTransaction.parse_obj(temp_item)
            db_output_trans = raw_account_transaction_dao.create(db=db, obj_in=raw_account_transaction)
            raw_trans_list.append(db_output_trans)

        return raw_trans_list
    except Exception as e:
        print("Exception", e)
        return []
