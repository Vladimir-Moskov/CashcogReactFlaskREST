"""
    Constantly Read from stream and write into DB in realtime
    Solution for
        - Consume the expense events provided by the Cashcog Expense-API. Validate and store them in a database of
        your choice.
"""

import requests
from app.config import Config
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

                Expense.query_add_from_json(line_obj)

                # logging as print for now
                print(loads(line))
            except (JSONDecodeError, TypeError) as error:

                print("%r" % error)

            else:
                pass
            finally:
                pass


if __name__ == '__main__':
    start_read_stream()



