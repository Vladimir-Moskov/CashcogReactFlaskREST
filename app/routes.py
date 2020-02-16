"""
    flask web application /CashcogReact-Expenses" routing / url mapping
        SERVER_NAME_WEB_APP = "/CashcogReact-Expenses"
        PORT_WEB_APP = "5000"

    React one page application - statrts here 127.0.0.1:5000/CashcogReact-Expenses/
"""
from flask import request
from flask import render_template
from app import app, app_blueprint
from app.models import Expense, Employee, ApplicationRequestLog, ApplicationType
from functools import wraps
from app.config import Config


def log_request(func):
    """
    user request logging decorator
    :param func: decorated function
    :return: decorator
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        ApplicationRequestLog.query_add(request, ApplicationType.WEB_APP.name)
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

# React app
@app_blueprint.route('/')
@app_blueprint.route('/index')
@log_request
def index():
    """
        Welcome page - enter point for React one page application
    :return:
    """
    # return render_template('index.html', title='Welcome here',  app_root=Config.SERVER_NAME_WEB_APP,)
    return render_template('frontend/index.html', title='Welcome here',  app_root=Config.SERVER_NAME_WEB_APP,)


# just plain html page for debug purpose
@app_blueprint.route('/expenses')
@log_request
def expenses():
    """
         Page with expenses data  from stream
    :return: plain html page
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('expenses.html',
                           app_root=Config.SERVER_NAME_WEB_APP,
                           title='Cashcog Expenses',
                           headers=Expense.headers(),
                           expenses_all=Expense.query_get_all())


# just plain html page for debug purpose
@app_blueprint.route('/employee')
@log_request
def employee():
    """
    Page with employees data  from stream
    :return: plain html page
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('employee.html',
                           app_root=Config.SERVER_NAME_WEB_APP,
                           title='Cashcog Employee',
                           headers=Employee.headers(),
                           employee_all=Employee.query_get_all())


# just plain html page for debug purpose
@app_blueprint.route('/log')
@log_request
def log():
    """
         Page with data from user requests log in order to solve -
         "On each GET/POST/PUT request, log that the data was requested (in the same database)"
    :return: plain html page
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('applicationLog.html',
                           app_root=Config.SERVER_NAME_WEB_APP,
                           title='Application Log',
                           headers=ApplicationRequestLog.headers(),
                           logs_all=ApplicationRequestLog.query_get_all())


app.register_blueprint(app_blueprint, url_prefix=Config.SERVER_NAME_WEB_APP)
