import json
import requests
from app.config import Config


def start_read_stream():
    r = requests.get(Config.CASHCOG_STREAM_URL, stream=True)
    for line in r.iter_lines():
        if line:
            print(json.loads(line))


if __name__ == '__main__':
    start_read_stream()



