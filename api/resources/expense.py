from flask_restful import reqparse, Resource
from app.models import Expense, Employee, ApplicationRequestLog, ExpenseSchema, EmployeeSchema
from flask import request

# parser = reqparse.RequestParser()
# parser.add_argument('expense_id', type=int, help='expense_id')
# args = parser.parse_args()


class ExpenseAPI(Resource):
    """

    """

    def get(self, expense_id=None):
        query_data = Expense.query_get_all(expense_id)
        result = ExpenseSchema().dump(query_data, many=(expense_id is None))
        return {'status': 'success', 'data': result}, 200

    def post(self):
        data = request.get_json()
        new_item = Expense.query_add_from_json(data)
        return data, 201

    def put(self, expense_id):
        data = request.get_json()
        return data, 201


class EmployeeAPI(Resource):
    """

    """

    def get(self, employee_id=None):
        query_data = Employee.query_get_all(employee_id)
        result = EmployeeSchema().dump(query_data, many=(employee_id is None))
        return {'status': 'success', 'data': result}, 200
