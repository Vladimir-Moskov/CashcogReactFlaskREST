import requests
from app.config import Config
from app.models import Expense
import json


def start_read_stream():
    r = requests.get(Config.CASHCOG_STREAM_URL, stream=True)
    for line in r.iter_lines():
        if line:
            line_obj = json.loads(line)
            Expense.query_add_from_json(line_obj)
            print(json.loads(line))


if __name__ == '__main__':
    start_read_stream()



