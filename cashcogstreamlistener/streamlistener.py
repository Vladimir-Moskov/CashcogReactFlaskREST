"""
    Constantly Read from stream and write into DB in realtime
    Solution for
        '- Consume the expense events provided by the Cashcog Expense-API. Validate and store them in a database of
        your choice.'
"""

import requests
from app.config import Config, StreamDataInjectionType
from app.models import Expense
from json import loads, JSONDecodeError
from multiprocessing import Process, Queue

# TODO: implement intervention reading external intervention


def start_read_stream():
    """
     Run stream reader in non stop
    :return: None
    """
    # Launch data saver as a separate python process in order to manage better heavy stream traffic
    entyties_queue: Queue = Queue()  # entities from stream
    # parallel process
    saver_proc: Process = Process(target=save_expense_from_stream, args=(entyties_queue,))
    saver_proc.daemon = True
    saver_proc.start()

    r = requests.get(Config.CASHCOG_STREAM_URL, stream=True)
    for expense_line in r.iter_lines():
        if expense_line:
            try:
                # save every item in process
                expense_obj = loads(expense_line)
                entyties_queue.put(expense_obj)
                print(f"new entity from stream {expense_obj['uuid']}")
            except (JSONDecodeError, TypeError) as error:
                print(f"{repr(error)}")
            # TODO: handle exceptions properly - replase placeholder with real code
            else:
                pass
            finally:
                pass


def save_expense_from_stream(entyties_queue: Queue):
    """
    save one expense item

        :param entyties_queue:
        :return:
    """
    # TODO: handle exceptions properly
    while True:
        try:
            expense_obj = entyties_queue.get()
            if expense_obj:
                # direct save into DB
                if Config.UPDATE_FROM_STREAM == StreamDataInjectionType.DIRECT_DB_DATA_INSERT:
                    Expense.query_add_from_json(expense_obj)
                    print(f"new entity saved into DB  {expense_obj['uuid']}")
                # USE 'microservices' approach
                elif Config.UPDATE_FROM_STREAM == StreamDataInjectionType.USE_API_POST_DATA:
                    post_expence_url = Config.EXPENSE_API_ADD
                    request_self = requests.post(url=post_expence_url, json=expense_obj)
                    try:
                        if request_self.status_code == 201:
                            print('Success!')
                            new_item = request_self.json()
                        else:
                            new_item = {'ERROR': request_self.status_code}

                        # logging as print for now
                        print(new_item)
                    except Exception as error:
                        print(f"ERROR: on save_expense_from_stream PUT = {repr(error)}")

        except Exception as error:
            print(f"{repr(error)}")


if __name__ == '__main__':
    start_read_stream()



