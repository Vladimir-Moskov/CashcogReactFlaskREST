
"""
    independent API  application itself - just run in to start server
    started on
        PORT_API_APP = "5001"
        SERVER_NAME_API_APP = "/cashcogXCNT/api/v1"
"""
from flask import Flask
from app.config import Config
from api.resources.expense import ExpenseAPI, EmployeeAPI, ExpenseApproveAPI, ApplicationRequestLogAPI
from flask_sqlalchemy import SQLAlchemy

from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

# createFlask app
app = Flask(__name__)
api = Api(app, prefix=Config.SERVER_NAME_API_APP)
# add CORS for frontend cross domain policy
cors = CORS(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

# url mapping below - api itself
api.add_resource(ExpenseAPI, '/expense/<expense_id>',  endpoint="expense", methods=['GET', 'PUT'])
api.add_resource(ExpenseAPI, '/expense',  endpoint="expense_post", methods=['POST'])
api.add_resource(ExpenseAPI, '/expenses',  endpoint="expenses", methods=['GET'])

api.add_resource(ExpenseApproveAPI, '/expense/<expense_id>/approve',  endpoint="expense_approve", methods=['PUT'])

api.add_resource(EmployeeAPI, '/employees',  endpoint="employees", methods=['GET'])
api.add_resource(EmployeeAPI, '/employee/<employee_id>',  endpoint="employee", methods=['GET'])

api.add_resource(ApplicationRequestLogAPI, '/logs',  endpoint="logs", methods=['GET'])

# start server
if __name__ == '__main__':
    app.run(port=Config.PORT_API_APP, debug=Config.DEBUG_GLOBAL)
