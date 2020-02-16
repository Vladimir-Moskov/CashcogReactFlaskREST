"""
   Web/API/Streamlistener  applications configuration variables
"""

import os
from enum import Enum

basedir = os.path.abspath(os.path.dirname(__file__))


class ApplicationType(Enum):
    """
        WEB_APP for web application requests log
        REST_API for api application requests log
    """
    WEB_APP = 1
    REST_API = 2


class StreamDataInjectionType(Enum):
    """
        how to handle/save data from stream - CASHCOG_STREAM_URL
    """
    DIRECT_DB_DATA_INSERT = 1
    USE_API_POST_DATA = 2


class Config(object):
    """
       applications general settings/variables
    """
    DEBUG_GLOBAL = True

    # wep app port and name
    SERVER_NAME_WEB_APP = "/CashcogReact-Expenses"
    PORT_WEB_APP = "5000"

    # wep app port
    PORT_API_APP = "5001"
    SERVER_NAME_API_APP = "/cashcogReact/api/v1"

    # Setup Database driver/ connect to DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'cashcog_expenses.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # stream urls settings
    CASHCOG_STREAM_URL = "https://cashcog.xcnt.io/stream"
    CASHCOG_SINGLE_URL = "https://cashcog.xcnt.io/single"

    # comment this line and uncomment the next one in order to use api for data insertion from stream
    UPDATE_FROM_STREAM = StreamDataInjectionType.DIRECT_DB_DATA_INSERT
    # Implement 'microservices' approach
    # UPDATE_FROM_STREAM = StreamDataInjectionType.USE_API_POST_DATA

    # save data service api for stream listener
    EXPENSE_API_ADD = f"http://127.0.0.1:{PORT_API_APP}{SERVER_NAME_API_APP}/expense"



