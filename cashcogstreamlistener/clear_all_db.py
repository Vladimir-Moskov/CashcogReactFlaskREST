"""
Use this script to clean data base in order to do full testing from scratch.
"""

from app.models import ApplicationRequestLog, Employee, Expense


def clean_db():
    """
      Run clean DB by using Flask ecosystem - just call model interface
    """
    ApplicationRequestLog.query_delete_all()
    Employee.query_delete_all()
    Expense.query_delete_all()


if __name__ == '__main__':
    clean_db()
