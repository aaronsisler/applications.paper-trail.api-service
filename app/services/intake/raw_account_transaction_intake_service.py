import humps
from sqlalchemy.orm import Session

from app.dao.raw_account_transaction_dao import raw_account_transaction_dao
from app.mappers.raw_account_transaction_mapper import RawAccountTransactionMapper
from app.models.raw_account_transaction import RawAccountTransaction
from app.utils.intake.csv_type_mapper import CsvTypeMapper


class RawAccountTransactionIntakeService:
    @staticmethod
    def intake(generic_list, account_id: int, user_id: int, db: Session):
        created_transactions = []

        for item in generic_list:
            # Use the CsvTypeMapper to convert types
            temp_item = CsvTypeMapper.map(vars(RawAccountTransactionMapper()), humps.decamelize(item))

            # Create models from mapper output
            raw_account_transaction = RawAccountTransaction.parse_obj(temp_item)
            # Save to database
            db_output_trans = raw_account_transaction_dao.create(db=db, obj_in=raw_account_transaction)

            # Return new record with creation id
            created_transactions.append(db_output_trans)

        return created_transactions
