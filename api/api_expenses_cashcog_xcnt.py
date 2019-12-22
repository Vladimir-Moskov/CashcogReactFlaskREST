# web application itself - just run in to start server
from flask import Flask
from app.config import Config
from api.resources.expense import Expense

from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app, prefix=Config.SERVER_NAME_API_APP)


api.add_resource(Expense,
                 # '/expenses',
                 '/expense/<expense_id>')

if __name__ == '__main__':
    # with app.app_context():
    #     # within this block, current_app points to app.
    #     print(app.name)

    app.run(debug=Config.DEBUG_GLOBAL)
    # host_name = app.name #+":"+str(Config.PORT_API_APP)
    # app.run(host=host_name, debug=Config.DEBUG_GLOBAL)
    # app.run(host=Config.SERVER_NAME_WEB_API, port=Config.PORT_API_APP)
