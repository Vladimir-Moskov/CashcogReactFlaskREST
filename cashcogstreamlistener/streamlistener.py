"""
    Constantly Read from stream and write into DB in realtime
    Solution for
        - Consume the expense events provided by the Cashcog Expense-API. Validate and store them in a database of
        your choice.
"""

import requests
from app.config import Config, StreamDataInjectionType
from app.models import Expense
from json import loads, JSONDecodeError


def start_read_stream():
    """

    :return: None
    """
    r = requests.get(Config.CASHCOG_STREAM_URL, stream=True)
    for line in r.iter_lines():
        if line:
            try:
                line_obj = loads(line)
                if Config.UPDATE_FROM_STREAM == StreamDataInjectionType.DIRECT_DB_DATA_INSERT:
                    Expense.query_add_from_json(line_obj)
                elif Config.UPDATE_FROM_STREAM == StreamDataInjectionType.USE_API_POST_DATA:
                    pass

                # logging as print for now
                print(loads(line))
            except (JSONDecodeError, TypeError) as error:
                print(f"{repr(error)}")

            else:
                pass
            finally:
                pass


if __name__ == '__main__':
    start_read_stream()



