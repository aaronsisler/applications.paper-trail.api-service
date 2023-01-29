from datetime import datetime
from enum import Enum


class DateParserFormat(str, Enum):
    MM_SLASH_DD_SLASH_YYYY = '%m/%d/%Y'


class DateParserUtil:
    @staticmethod
    def parse_date(date_string: str, date_format: str) -> datetime:
        return datetime.strptime(date_string, date_format)
