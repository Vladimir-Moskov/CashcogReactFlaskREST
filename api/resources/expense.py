from flask_restful import reqparse, Resource
from app.models import Expense, Employee, ApplicationRequestLog
from app.models import ExpenseSchema, EmployeeSchema, ApplicationRequestLogSchema
from flask import request

# parser = reqparse.RequestParser()
# parser.add_argument('expense_id', type=int, help='expense_id')
# args = parser.parse_args()


class ExpenseAPI(Resource):
    """

    """

    def get(self, expense_id: int = None):
        query_data = Expense.query_get_all(expense_id)
        result = ExpenseSchema().dump(query_data, many=(expense_id is None))
        return {'status': 'success', 'data': result}, 200

    def post(self):
        data = request.get_json()
        result = ExpenseSchema().dump(Expense.query_add_from_json(data), many=False)
        return {'status': 'success', 'data': result}, 201

    # TODO implement put properly
    def put(self, expense_id: int):
        data = request.get_json()
        result = ExpenseSchema().dump(Expense.query_add_from_json(data), many=False)
        return {'status': 'success', 'data': result}, 201


class ExpenseApproveAPI(Resource):
    """

    """

    def put(self, expense_id: int):
        data = request.get_json()
        result = ExpenseSchema().dump(Expense.query_approve_from_json(expense_id, data), many=False)
        return {'status': 'success', 'data': result}, 201


class EmployeeAPI(Resource):
    """

    """

    def get(self, employee_id: int = None):
        query_data = Employee.query_get_all(employee_id)
        result = EmployeeSchema().dump(query_data, many=(employee_id is None))
        return {'status': 'success', 'data': result}, 200


class ApplicationRequestLogAPI(Resource):
    """

    """
    def get(self):
        top = request.args.get('top', 100)
        query_data = ApplicationRequestLog.query_get_all(top)
        result = ApplicationRequestLogSchema().dump(query_data, many=True)
        return {'status': 'success', 'data': result}, 200, {'Access-Control-Allow-Origin': '*'}
