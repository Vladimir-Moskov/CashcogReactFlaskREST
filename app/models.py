# typical flask model setup
from app import db
from datetime import datetime
from enum import Enum


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
                                        remote_user=request.remote_user)
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
        Table to store user requests for "On each GET request, log that the data was requested (in the same database)"
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
    def query_add(uuid, first_name, last_name):
        exists = Employee.query.filter_by(id=uuid).first()
        if exists:
            exists.first_name = first_name
            exists.last_name = last_name
        else:
            timestamp_datetime = datetime.now()
            new_row = Employee(uuid=uuid, first_name=first_name, last_name=last_name, created_at=timestamp_datetime)
            db.session.add(new_row)
        db.session.commit()

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers():
        """

        :return: list of headers names for ui
        """
        return ["ID", "TIMESTAMP", "IP", "URL", "METHOD", "AGENT", "USER"]


class Expense(db.Model):
    """
        Table SteelProcessing - store data model from file task_data.csv

        "uuid": "92b19fc6-5386-4985-bf5c-dc56c903dd23",
"description": "Itaque fugiat repellendus velit deserunt praesentium.",
"created_at": "2019-09-22T23:07:01",
"amount": 2291,
"currency": "UZS",
"employee"
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=False)
    uuid = db.Column(db.String(36), index=True, unique=True, nullable=False)
    description = db.Column(db.String(4000))
    created_at = db.Column(db.DateTime, index=False, unique=False)
    currency = db.Column(db.String(4))
    amount = db.Column(db.Float, default=0)


    def __repr__(self):
        return '<SteelProcessing: id:{}, timestamp:{}, temperature:{}, duration:{}>'.\
            format(self.id, self.timestamp, self.temperature, self.duration)

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers():
        """

        :return: list of headers names for ui
        """
        return ["ID", "TIMESTAMP", "TEMPERATURE", "DURATION"]

    @staticmethod
    def query_get_all():
        return Employee.query.all()

    @staticmethod
    def query_delete_all():
        Employee.query.delete()
        db.session.commit()

    @staticmethod
    def query_add_by_id(id, timestamp, temperature, duration):
        # check if row with the same id already exists
        exists = Employee.query.filter_by(id=id).first()
        if not exists:
            timestamp_datetime = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            new_row = Employee(id=id, timestamp=timestamp_datetime, temperature=temperature, duration=duration)
            db.session.add(new_row)
            db.session.commit()
        return exists
