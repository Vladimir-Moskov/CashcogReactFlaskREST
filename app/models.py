"""
    ORM - typical flask model setup
    ApplicationRequestLog for logs
    Expense for records from given stream service -
    Employee for Employee sub-object of Expense from given stream service
"""
from app import db, marshmallow
from datetime import datetime
from app.config import ApplicationType
from enum import Enum
from typing import List, Optional, Any, Dict


class ApplicationRequestLog(db.Model):
    """
        Table to store user requests for "On each GET/PUT/POST request, log that the data was requested
        (in the same database)
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, index=True, unique=False, default=datetime.now())
    remote_addr = db.Column(db.String(100))
    url = db.Column(db.String(1000))
    method = db.Column(db.String(10))
    user_agent = db.Column(db.String(100))
    remote_user = db.Column(db.String(100))
    application_type = db.Column(db.String(10))

    def __repr__(self) -> str:
        """
           Standard customization of class instance to string
           :return: string representation of object
        """
        return f'<ApplicationRequestLog: id:{self.id}, timestamp:{self.timestamp}, ' \
               f'remote_address:{self.remote_address}, url:{self.url} remote_user:{self.remote_user}, ' \
               f'user_agent:{self.user_agent}>'

    @classmethod
    def query_get_all(cls, top: int = 100) -> Optional[Any]:
        """
        get all logs records from DB
        :param top: amount of records
        :return: data from db
        """
        return cls.query.order_by(cls.timestamp.desc()).limit(top).all()

    @classmethod
    def query_delete_all(cls) -> None:
        """
         delete all logs records, part of clean data from DB
        """
        cls.query.delete()
        db.session.commit()

    @classmethod
    def query_add(cls, request, application_type=ApplicationType.WEB_APP.name) -> None:
        """
        create log entity from request in DB
        :param request: http request from web/api application
        :param application_type:  web or api
        :return: None
        """
        new_row = cls(remote_addr=request.remote_addr,
                      url=request.url,
                      method=request.method,
                      user_agent=str(request.user_agent),
                      remote_user=request.remote_user,
                      application_type=application_type)
        db.session.add(new_row)
        db.session.commit()

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers() -> List[str]:
        """
        headers for frontend
        :return: list of headers names for ui
        """
        return ["ID", "TIMESTAMP", "IP", "URL", "METHOD", "AGENT", "USER", "APP. TYPE"]


class Employee(db.Model):
    """
        Data model/Table to store employees

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

    def __repr__(self) -> str:
        """
           Standard customization of class instance to string
           :return: string representation of object
        """
        return f'<Employee: id:{self.id}, uuid:{self.uuid}, first_name:{self.first_name}, last_name:{self.last_name},' \
               f' created_at:{self.created_at}>'

    @classmethod
    def query_get_all(cls, employee_id: int = None) -> Optional[Any]:
        """
        get employees data from DB
        :param employee_id: optional, to get specific employee
        :return:
        """
        if employee_id:
            return cls.query.filter_by(id=employee_id).first()
        else:
            return cls.query.all()

    @classmethod
    def query_delete_all(cls) -> None:
        """
         delete all employees records, part of clean data from DB
        """
        cls.query.delete()
        db.session.commit()

    @classmethod
    def add_item(cls, employee_item: Dict) -> int:
        """
        create employee from json/dic
        :param employee_item: employee data
        :return: id of new row
        """
        new_id = 0
        try:
            new_id = cls.query_add(employee_item["uuid"],  employee_item["first_name"], employee_item["last_name"])
        except Exception as error:
            print(f"{repr(error)}")
        return new_id

    @classmethod
    def query_add(cls, uuid: str, first_name: str, last_name: str) -> int:
        """
        create employee in DB
        :param uuid:
        :param first_name:
        :param last_name:
        :return: id of new row
        """
        new_row = cls.query.filter_by(uuid=uuid).first()
        if new_row:
            new_row.first_name = first_name
            new_row.last_name = last_name
        else:
            timestamp_datetime = datetime.now()
            new_row = cls(uuid=uuid, first_name=first_name, last_name=last_name, created_at=timestamp_datetime)
            db.session.add(new_row)
        db.session.commit()
        return new_row.id

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers() -> List[str]:
        """
        headers for frontend
        :return: list of headers names for ui
        """
        return ["ID", "UUID", "FIRST NAME", "LAST NAME", "CREATED AT"]


class ApproveStateEnum(Enum):
    """
    expense status values
    """
    NOT_SET = 0
    APPROVED = 1
    DECLINED = 2


class Expense(db.Model):
    """
        Table Expense - store data model for Expenses object from stream service

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
    created_at = db.Column(db.DateTime, index=False, unique=False, default=datetime.now)
    currency = db.Column(db.String(4), nullable=False)
    amount = db.Column(db.Float, default=0)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship("Employee", backref=db.backref("expense", uselist=False))

    # TODO: as it uses sqllite for now - TYINT, BIT or SHORT type not available for 3 states column
    # Here is not normalized approach
    approve_state = db.Column(db.Integer, default=ApproveStateEnum.NOT_SET.value)
    # 'user name' - should be user id
    approved_by = db.Column(db.String(100), nullable=True)
    approved_datetime = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        """
           Standard customization of class instance to string
           :return: string representation of object
        """
        return f'<Expense: id:{self.id}, uuid:{self.uuid}, description:{self.description}, ' \
               f'created_at:{self.created_at}, ' \
               f'currency:{self.currency}, amount:{self.amount}, approve_state:{self.approve_state}, ' \
               f'approved_by:{self.approved_by}, approved_datetime:{self.approved_datetime}>'

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers() -> List[str]:
        """
        headers for frontend
        :return: list of headers names for ui
        """
        return ["ID", "UUID", "DESCRIPTION", "CREATED AT", "CURRENCY", "AMOUNT", "APPROVE", "APPROVED_BY",
                "APPROVED_TIME"]

    @classmethod
    def query_get_all(cls, expense_id: int = None) -> Optional[Any]:
        """
        get all expenses from DB
        :param expense_id: expense id
        :return: None
        """
        if expense_id:
            return cls.query.filter_by(id=expense_id).first()
        else:
            return cls.query.all()

    @classmethod
    def query_get_all_join_employee(cls) -> Optional[Any]:
        """
        get expenses data with joined employee
        :return: records from DB
        """
        records = cls.query.join(Employee).all()
        return records

    @classmethod
    def query_delete_all(cls) -> None:
        """
        delete all expenses records, part of clean data from DB
        :return: None
        """
        cls.query.delete()
        db.session.commit()

    @classmethod
    def query_add(cls, uuid: str,
                  description: str,
                  created_at,
                  currency: str,
                  amount: float,
                  employee_id: int) -> Optional[Any]:
        """
        add expense item into DB

        :param uuid:
        :param description:
        :param created_at:
        :param currency:
        :param amount:
        :param employee_id:
        :return: is expense has already been created
        """
        # check if row with the same id already exists
        exists = cls.query.filter_by(uuid=uuid).first()
        if not exists:
            # timestamp_created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
            new_row = cls(uuid=uuid,
                          description=description,
                          created_at=created_at,
                          currency=currency,
                          amount=amount,
                          employee_id=employee_id)
            db.session.add(new_row)
            db.session.commit()
        return exists

    @classmethod
    def add_item(cls, expense_item: Dict, employee_id: int) -> Optional[Any]:
        """
        add expense item from data object
        :param expense_item:
        :param employee_id:
        :return: new record from DB
        """
        try:
            created_at = datetime.strptime(expense_item["created_at"], '%Y-%m-%dT%H:%M:%S')
            result = cls.query_add(uuid=expense_item["uuid"],
                                   description=expense_item["description"],
                                   created_at=created_at,
                                   currency=expense_item["currency"],
                                   amount=expense_item["amount"],
                                   employee_id=employee_id)
        except Exception as error:
            print(f"{repr(error)}")
            result = None
        finally:
            pass

        return result

    @classmethod
    def query_add_from_json(cls, json_item: Dict) -> None:
        """
         add expense item from json object
        :param json_item: expense as json
        :return: None
        """
        try:
            new_employee_id = Employee.add_item(json_item["employee"])
            if new_employee_id > 0:
                cls.add_item(json_item, new_employee_id)
        except Exception as error:
            print(f"ERROR: add_from_json = {repr(error)}")

    @classmethod
    def query_approve(cls, expense_id: int, approve_state: int, approved_by: str) -> None:
        """
        change approved state of expense in DB
        :param expense_id:
        :param approve_state: new approved state
        :param approved_by: approved user
        :return: None
        """
        expense = Expense.query.filter_by(id=expense_id).first()
        expense.approve_state = approve_state
        expense.approved_by = approved_by
        expense.approved_datetime = datetime.now()
        db.session.commit()

    @classmethod
    def query_approve_from_json(cls, expense_id: int, json_item: Dict) -> None:
        """
         change approved state of expense for json
        :param expense_id:
        :param json_item:
        :return:
        """
        try:
            new_status = json_item['approve']  # TODO: validate value
            # new_status = ApproveStateEnum[json_item['approve']].value
            # user = json_item['user']
            user = "current_user"
            cls.query_approve(expense_id, new_status, user)
        except Exception as error:
            print(f"ERROR: add_from_json = {repr(error)}")
        print(json_item)


class ExpenseSchema(marshmallow.ModelSchema):
    """
    use it for Expense serialization
    """
    class Meta:
        model = Expense


class EmployeeSchema(marshmallow.ModelSchema):
    """
       use it for employee serialization
    """
    class Meta:
        model = Employee


class ApplicationRequestLogSchema(marshmallow.ModelSchema):
    """
        use it for log serialization
    """
    class Meta:
        model = ApplicationRequestLog
