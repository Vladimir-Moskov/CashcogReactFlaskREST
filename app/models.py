"""
    ORM - typical flask model setup
    ApplicationRequestLog for logs
    SteelProcessing for records from given file with data
"""
from app import db
from datetime import datetime
from enum import Enum


# flask db migrate -m "ApplicationRequestLog table"
class ApplicationType(Enum):
    WEB_APP = 'WEB_APP'
    REST_API = 'REST_API'


class ApplicationRequestLog(db.Model):
    """
        Table to store user requests for "On each GET request, log that the data was requested (in the same database)"
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, index=True, unique=False)
    remote_addr = db.Column(db.String(100))
    url = db.Column(db.String(1000))
    method = db.Column(db.String(10))
    user_agent = db.Column(db.String(100))
    remote_user = db.Column(db.String(100))
    application_type = db.Column(db.String(10))

    def __repr__(self):
        """
           Standard customization of class instance to string
           :return: string representation of object
        """
        return '<ApplicationRequestLog: id:{}, timestamp:{}, remote_address:{}, remote_user:{}, user_agent:{}>'. \
            format(self.id, self.timestamp, self.remote_address, self.url, self.remote_user, self.user_agent)


    @staticmethod
    def query_get_all():
        return ApplicationRequestLog.query.all()


    @staticmethod
    def query_delete_all():
        ApplicationRequestLog.query.delete()
        db.session.commit()


    @staticmethod
    def query_add(request):
        timestamp_datetime = datetime.now()
        new_row = ApplicationRequestLog(timestamp=timestamp_datetime,
                                        remote_addr=request.remote_addr,
                                        url=request.url,
                                        method=request.method,
                                        user_agent=str(request.user_agent),
                                        remote_user=request.remote_user,
                                        application_type=ApplicationType.WEB_APP)
        db.session.add(new_row)
        db.session.commit()


    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers():
        """

        :return: list of headers names for ui
        """
        return ["ID", "TIMESTAMP", "IP", "URL", "METHOD", "AGENT", "USER", "APP. TYPE"]


class Employee(db.Model):
    """
        Table to store user requests for "On each GET request, log that the data was requested (in the same database)

        "employee": {
        "uuid": "858142ac-299a-48f0-b221-7d6de9439454",
        "first_name": "Birthe",
        "last_name": “Meier"
        }
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=False)
    uuid = db.Column(db.String(36), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, index=False, unique=False)

    def __repr__(self):
        return '<ApplicationRequestLog: id:{}, uuid:{}, first_name:{}, last_name:{}, created_at:{}>'.\
            format(self.id, self.uuid, self.first_name, self.last_name, self.created_at)

    @staticmethod
    def query_get_all():
        return Employee.query.all()

    @staticmethod
    def query_delete_all():
        Employee.query.delete()
        db.session.commit()

    @staticmethod
    def add_item(employee_item):
        new_id = 0
        #try:
        new_id = Employee.query_add(employee_item["uuid"],  employee_item["first_name"], employee_item["last_name"])
        #except:
        #    pass
        return new_id

    @staticmethod
    def query_add(uuid, first_name, last_name):
        new_row = Employee.query.filter_by(uuid=uuid).first()
        new_id = 0
        if new_row:
            new_row.first_name = first_name
            new_row.last_name = last_name

        else:
            timestamp_datetime = datetime.now()
            new_row = Employee(uuid=uuid, first_name=first_name, last_name=last_name, created_at=timestamp_datetime)
            db.session.add(new_row)
        db.session.commit()
        return new_row.id

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers():
        """

        :return: list of headers names for ui
        """
        return ["ID", "UUID", "FIRST NAME", "LAST NAME", "CREATED AT"]


class Expense(db.Model):
    """
        Table SteelProcessing - store data model from file task_data.csv

        "uuid": "92b19fc6-5386-4985-bf5c-dc56c903dd23",
        "description": "Itaque fugiat repellendus velit deserunt praesentium.",
        "created_at": "2019-09-22T23:07:01",
        "amount": 2291,
        "currency": "UZS",
        "employee"{}
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=False)
    uuid = db.Column(db.String(36), index=True, unique=True, nullable=False)
    description = db.Column(db.String(4000))
    created_at = db.Column(db.DateTime, index=False, unique=False)
    currency = db.Column(db.String(4))
    amount = db.Column(db.Float, default=0)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    employee = db.relationship("Employee", backref=db.backref("employee", uselist=False))

    def __repr__(self):
        return '<SteelProcessing: id:{}, uuid:{}, description:{}, created_at:{}, currency:{}, amount:{}>'.\
            format(self.id, self.uuid, self.description, self.created_at, self.currency, self.amount)

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers():
        """

        :return: list of headers names for ui
        """
        return ["ID", "UUID", "DESCRIPTION", "CREATED AT", "CURRENCY", "AMOUNT"]

    @staticmethod
    def query_get_all():
        return Expense.query.all()

    @staticmethod
    def query_get_all_join_employee():
        records = Expense.query.join(Employee).all()
        return records

    @staticmethod
    def query_delete_all():
        Expense.query.delete()
        db.session.commit()

    @staticmethod
    def query_add(uuid, description, created_at, currency, amount, employee_id):
        # check if row with the same id already exists
        exists = Employee.query.filter_by(uuid=uuid).first()
        if not exists:
            timestamp_created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f')
            new_row = Expense(uuid=uuid,
                              description=description,
                              created_at=timestamp_created_at,
                              currency=currency,
                              amount=amount,
                              employee_id=employee_id)
            db.session.add(new_row)
            db.session.commit()
        return exists

    @staticmethod
    def add_item(expense_item, employee_id):
        Expense.query_add(uuid=expense_item["uuid"],
                          description=expense_item["description"],
                          created_at=expense_item["created_at"],
                          currency=expense_item["currency"],
                          amount=expense_item["amount"],
                          employee_id=employee_id)


    @staticmethod
    def query_add_from_json(json_item):
        #try:
        new_employee_id = Employee.add_item(json_item["employee"])
        if new_employee_id > 0:
            Expense.add_item(json_item, new_employee_id)
        #except:
        #    pass
        print(json_item)
