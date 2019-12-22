from flask_restful import reqparse, Resource

parser = reqparse.RequestParser()
parser.add_argument('expense_id', type=int, help='Rate to charge for this resource')
args = parser.parse_args()

class Expense(Resource):
    def get(self, expense_id):
        # abort_if_todo_doesnt_exist(todo_id)
        return {expense_id: '1'}, 200  # TODOS[todo_id]

    def put(self, expense_id):
        #args = parser.parse_args()
        # task = {'task': args['expense_id']}
        task = {'task': 'expense_id'}
        # TODOS[todo_id] = task
        return task, 201