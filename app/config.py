# flask application configuration variable

import os
from enum import Enum

basedir = os.path.abspath(os.path.dirname(__file__))


class ApplicationType(Enum):
    WEB_APP = 1
    REST_API = 2


class StreamDataInjectionType(Enum):
    DIRECT_DB_DATA_INSERT = 1
    USE_API_POST_DATA = 2


class Config(object):
    DEBUG_GLOBAL = True

    # wep app port and name
    SERVER_NAME_WEB_APP = "/CashcogXCNT-Expenses"
    PORT_WEB_APP = "5000"

    # wep app port
    PORT_API_APP = "5001"
    SERVER_NAME_API_APP = "/cashcogXCNT/api/v1"

    # Setup Database driver/ connect to DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'cashcog_expenses.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # stream urls
    CASHCOG_STREAM_URL = "https://cashcog.xcnt.io/stream"
    CASHCOG_SINGLE_URL = "https://cashcog.xcnt.io/single"

    UPDATE_FROM_STREAM = StreamDataInjectionType.DIRECT_DB_DATA_INSERT
    # APPLICATION_ROOT = SERVER_NAME_WEB_APP
    # SCRIPT_NAME = SERVER_NAME_WEB_APP
    # SERVER_NAME = 'localhost:' + PORT_WEB_APP


