from flask_restful import reqparse, Resource
from app.models import Expense, Employee, ApplicationRequestLog, ExpenseSchema

parser = reqparse.RequestParser()
parser.add_argument('expense_id', type=int, help='expense_id')
args = parser.parse_args()


class ExpenseAPI(Resource):
    """

    """

    def get(self, expense_id=None):
        query_data = Expense.query_get_all(expense_id)
        result = ExpenseSchema().dump(query_data, many=(expense_id is None))
        return {'status': 'success', 'data': result}, 200

    def put(self, expense_id):
        #args = parser.parse_args()
        # task = {'task': args['expense_id']}
        task = {'task': 'expense_id'}
        # TODOS[todo_id] = task
        return {'status': 'success', 'data': task}, 201
