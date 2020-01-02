from flask import request
from flask import render_template
from app import app, app_blueprint
from app.models import Expense, Employee, ApplicationRequestLog
from functools import wraps
from app.config import Config


# user request logging decorator
def log_request(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        ApplicationRequestLog.query_add(request, )
        return func(*args, **kwargs)

    return decorated


@log_request
@app.errorhandler(404)
def not_found(e):
    """
         use template made by Colorlib (https://colorlib.com)
        :param e: request
        :return: error page wrapper
    """
    return render_template('404.html', app_root=Config.SERVER_NAME_WEB_APP), 404


@app_blueprint.route('/')
@app_blueprint.route('/index')
@log_request
def index():
    """
        Welcome page
    :return:
    """
    # return render_template('index.html', title='Welcome here',  app_root=Config.SERVER_NAME_WEB_APP,)
    return render_template('frontend/index.html', title='Welcome here',  app_root=Config.SERVER_NAME_WEB_APP,)

@app_blueprint.route('/expenses')
@log_request
def expenses():
    """
         Page with data from task_data.csv in order to solve
         Serve the database data (from `task_data.csv`) in a _simple_ html format
    :return:
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('expenses.html',
                           app_root=Config.SERVER_NAME_WEB_APP,
                           title='XCNT Expenses',
                           headers=Expense.headers(),
                           expenses_all=Expense.query_get_all())


@app_blueprint.route('/employee')
@log_request
def employee():
    """
         Page with data from task_data.csv in order to solve
         Serve the database data (from `task_data.csv`) in a _simple_ html format
    :return:
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('employee.html',
                           app_root=Config.SERVER_NAME_WEB_APP,
                           title='XCNT Employee',
                           headers=Employee.headers(),
                           employee_all=Employee.query_get_all())


@app_blueprint.route('/log')
@log_request
def log():
    """
         Page with data from user requests log in order to solve -
         "On each GET request, log that the data was requested (in the same database)"
    :return:
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('applicationLog.html',
                           app_root=Config.SERVER_NAME_WEB_APP,
                           title='Application Log',
                           headers=ApplicationRequestLog.headers(),
                           logs_all=ApplicationRequestLog.query_get_all())


app.register_blueprint(app_blueprint, url_prefix=Config.SERVER_NAME_WEB_APP)
