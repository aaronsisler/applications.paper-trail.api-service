import base64
import csv


class CsvFileParser:
    @staticmethod
    def parse(base64_encoded_file: str):
        base64_message = base64_encoded_file.replace("data:text/csv;base64,", "")

        bytes_message = base64.b64decode(base64_message)
        message_lines = str(bytes_message, "utf-8").splitlines()

        reader = csv.DictReader(message_lines, delimiter=',')

        return list(reader)
