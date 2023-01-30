from sqlalchemy.orm import Session

from app.dao.raw_account_transaction_dao import raw_account_transaction_dao
from app.mappers.citi_raw_transaction_field_type_mapper import CitiRawTransactionFieldTypeMapper
from app.models.intake.intake_raw_account_transaction_request import IntakeRawAccountTransactionRequest
from app.models.intake.raw_account_transaction import RawAccountTransaction
from app.utils.date_parser_util import DateParserUtil, DateParserFormat
from app.utils.intake.csv_type_mapper import CsvTypeMapper


class CitiRawAccountTransactionIntakeService:
    @staticmethod
    def intake(generic_list: list, intake_request: IntakeRawAccountTransactionRequest, db: Session):
        created_transactions = []

        for item in generic_list:
            # Use the CsvTypeMapper to convert types
            temp_item = CsvTypeMapper.map(vars(CitiRawTransactionFieldTypeMapper()), item)

            # Parse fields to be correct formats
            amount = temp_item["Debit"] if temp_item["Debit"] else temp_item["Credit"]
            is_pending = False if temp_item["Status"] == "Cleared" else True

            # Parse out the datetime from raw trans date
            trans_date = DateParserUtil.parse_date(temp_item["Date"], DateParserFormat.MM_SLASH_DD_SLASH_YYYY)

            # Create models from mapper output
            raw_account_transaction = RawAccountTransaction(
                user_id=intake_request.user_id,
                account_id=intake_request.account_id,
                amount=amount,
                account_transaction_date=str(trans_date.date()),
                account_transaction_year=trans_date.year,
                account_transaction_month=trans_date.month,
                account_transaction_day=trans_date.day,
                is_pending=is_pending,
                merchant_name=temp_item["Description"],
                merchant_name_detailed=temp_item["Description"],
                categories=None
            )

            # Save to database
            db_output_trans = raw_account_transaction_dao.create(db=db, obj_in=raw_account_transaction)

            # Return new record with creation id
            created_transactions.append(db_output_trans)

        return created_transactions
