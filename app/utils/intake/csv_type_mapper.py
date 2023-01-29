from decimal import Decimal

from app.models.mapper_type import MapperType


class CsvTypeMapper:
    @staticmethod
    def map(mapper, raw_object):
        temp_item = {}

        try:
            for key in raw_object:

                if mapper[key] == MapperType.DECIMAL:
                    if not raw_object[key]:
                        temp_item[key] = None
                    else:
                        temp_item[key] = Decimal(raw_object[key])
                elif mapper[key] == MapperType.INTEGER:
                    temp_item[key] = int(raw_object[key])
                elif mapper[key] == MapperType.BOOLEAN:
                    temp_item[key] = eval(raw_object[key])
                else:
                    temp_item[key] = raw_object[key]

            return temp_item
        except Exception as e:
            print("Exception", e)
