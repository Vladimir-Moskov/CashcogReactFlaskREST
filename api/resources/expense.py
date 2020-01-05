"""
    RESTFull flask resources, data model of API
"""

from flask_restful import reqparse, Resource
from app.models import Expense, Employee, ApplicationRequestLog, ApplicationType
from app.models import ExpenseSchema, EmployeeSchema, ApplicationRequestLogSchema
from flask import request
from functools import wraps

# use {'Access-Control-Allow-Origin': '*'} for cross domain policy


def log_request(func):
    """
    user request logging decorator
    :param func: decorated function
    :return: decorator
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        ApplicationRequestLog.query_add(request, ApplicationType.REST_API.name)
        return func(*args, **kwargs)

    return decorated


class ExpenseAPI(Resource):
    """
        ExpenseAPI interface
    """
    @log_request
    def get(self, expense_id: int = None):
        """
        Get one Expense item by id
        :param expense_id:
        :return: JSON data, response code, header
        """
        query_data = Expense.query_get_all(expense_id)
        result = ExpenseSchema().dump(query_data, many=(expense_id is None))
        return {'status': 'success', 'data': result}, 200, {'Access-Control-Allow-Origin': '*'}

    @log_request
    def post(self):
        """
        create new Expense item
        :return: JSON data, response code, header
       """
        data = request.get_json()
        result = ExpenseSchema().dump(Expense.query_add_from_json(data), many=False)
        return {'status': 'success', 'data': result}, 201, {'Access-Control-Allow-Origin': '*'}

    # TODO implement put properly
    @log_request
    def put(self, expense_id: int):
        """
        Update Expense item by id
        :param expense_id:
        :return:  JSON data, response code, header
        """
        data = request.get_json()
        result = ExpenseSchema().dump(Expense.query_add_from_json(data), many=False)
        return {'status': 'success', 'data': result}, 201, {'Access-Control-Allow-Origin': '*'}


class ExpenseApproveAPI(Resource):
    """
        Approve/Disapprove Expense API interface
    """

    @log_request
    def put(self, expense_id: int):
        """
        update expense status Approved/Not Approved by expense_id
        :param expense_id:
        :return:  JSON data, response code, header
        """
        data = request.get_json()
        result = ExpenseSchema().dump(Expense.query_approve_from_json(expense_id, data), many=False)
        return {'status': 'success', 'data': result}, 201, {'Access-Control-Allow-Origin': '*'}


class EmployeeAPI(Resource):
    """
       Employee API interface
    """

    @log_request
    def get(self, employee_id: int = None):
        """
        Get one Employee by id
        :param employee_id:
        :return: JSON data, response code, header
        """
        query_data = Employee.query_get_all(employee_id)
        result = EmployeeSchema().dump(query_data, many=(employee_id is None))
        return {'status': 'success', 'data': result}, 200, {'Access-Control-Allow-Origin': '*'}


class ApplicationRequestLogAPI(Resource):
    """
     Application Request Log API
    """
    @log_request
    def get(self):
        """
         GEt all logs entities
        :return:  JSON data, response code, header
        """
        top = request.args.get('top', 100)
        query_data = ApplicationRequestLog.query_get_all(top)
        result = ApplicationRequestLogSchema().dump(query_data, many=True)
        return {'status': 'success', 'data': result}, 200, {'Access-Control-Allow-Origin': '*'}
