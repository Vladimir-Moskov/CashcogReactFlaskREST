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
from multiprocessing import Process


def start_read_stream():
    """

    :return: None
    """
    r = requests.get(Config.CASHCOG_STREAM_URL, stream=True)
    for line in r.iter_lines():
        if line:

            try:
                line_obj = loads(line)
                local_process = Process(target=save_expence_from_stream, args=(line_obj,))
                local_process.start()
            except (JSONDecodeError, TypeError) as error:
                print(f"{repr(error)}")

            else:
                pass
            finally:
                pass


def save_expence_from_stream(line_obj):
    """

    :param line_obj:
    :return:
    """
    # TODO: handle exceptions properly
    try:
        if Config.UPDATE_FROM_STREAM == StreamDataInjectionType.DIRECT_DB_DATA_INSERT:
            new_item = Expense.query_add_from_json(line_obj)
        elif Config.UPDATE_FROM_STREAM == StreamDataInjectionType.USE_API_POST_DATA:
            post_expence_url = 'http://127.0.0.1:5001/cashcogXCNT/api/v1/expense'
            request_self = requests.post(url=post_expence_url, json=line_obj)
            if request_self.status_code == 201:
                print('Success!')
                new_item = request_self.json()
            else:
                new_item = {'ERROR': request_self.status_code}
            # logging as print for now
        print(new_item)
    except Exception as error:
        print(f"{repr(error)}")


if __name__ == '__main__':
    start_read_stream()



