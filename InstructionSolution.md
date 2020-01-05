# TODO: join employee for expense table
# TODO: table filter/query/sort

# Here is solution
  1. Flask ecosystem has been used to implement task
  2. SQLAlchemy and ORM to deal with data model
  3. flask_migrate Migrate to manage DB changes(add/update/delete table/field/model)
  4. single page web application page mapping in app/routes -
            SERVER_NAME_WEB_APP = "/CashcogXCNT-Expenses"
            PORT_WEB_APP = "5000"
  5. api application endpoint here
        PORT_API_APP = "5001"
        SERVER_NAME_API_APP = "/cashcogXCNT/api/v1"
  6. stream listener/reader - here ./cashcogstreamlistener

# The simple architecture behind this

    InterviewXCNTGmbH (source code root)
        |
        |--- api ( micro service - rest api application )
            |
            |--- resources ("data model"/ controller)
            |    |--- expense.py (implementation "data model")
            |
            |--- api_api_expenses_cashcog_xcnt.py (requests routing - controller)

        |--- app (web application + flask infrastructural components)
            |
            |--- frontend (all REACT front end there)
            |   |--- ....
            |--- static (some static files (*.css, *.js, *.ico) for frontend)
            |   |--- ....
            |--- templates (plain html pages - for debugging purpose)
            |   |--- ....
            |
            |--- __init__.py (Flask app setup - imports)
            |
            |--- app_expenses_cashcog_xcnt.py (run it to start web application )
            |
            |--- cashcog_expenses.db (SQLLite db file)
            |
            |--- config.py (application configuration and setting variables)
            |
            |--- models.py (ORM - applications data model)
            |
            |--- routes (web application url mapping)

        |--- cashcogstreamlistener (application to read data from stream)
            |
            |--- clear_all_db.py (simple clean db script, just for case)
            |
            |--- streamlistener.py (start this app to read and save data from stream)

## Project repository
> https://github.com/Vladimir-Moskov/InterviewXCNTGmbH

## From point of view MVP (Minimum Valuable Product)

1. For simplicity - logging has not been added
> TODO: add real life logging

2. For simplicity - unit tests and integration tests has not been implemented as well
> TODO: add real life tests with pytest

3. For simplicity - there is no any authorization/security
> TODO: implement it

4. TODO: fix time zone

5. # TODO: add better exception handling


## Project setup steps (Windows only)

 1. download project into your local disc or do VCS - Check out from version
    if you use Pycharm

 2. Install latest Python 3.7 if you do not have [https://realpython.com/installing-python/]
    and run cmd console

 3. Install pip  use command
   > python get-pip.py
   or follow step by step [https://www.liquidweb.com/kb/install-pip-windows/]

 4. Install Python virtualenv with command
   > pip install virtualenv

 5. set project folder as you current folder
    > cd   your_local_folder/InterviewXCNTGmbH

 6. Run next command in order to create virtualenv for project
   > virtualenv venv

 7. Activate virtual environment
   > your_local_folder/InterviewXCNTGmbH/venv/Scripts/activate

 8. install project dependencies

   > pip install -r requirements.txt

    and use

    > pip freeze > ../../requirements.txt

    in order to update list of project libraries
    and use

    > pip install <package-name>

    in case you miss some module

 9. You do not need to setup/update DB - it has been added in to repository
   > Data Base: sql lite in file InterviewXCNTGmbH/app/cashcog_expenses.db
   Here are some commands how to dial with it in case you want to do modifications
    > flask db init

    > flask db migrate -m "ApplicationRequestLog table"
    > flask db migrate -m "Expense table"
    > flask db migrate -m "Employee table"

    > flask db migrate

    > flask db upgrade

 10.

## Front end setup (React-Redux single page application)

   1. install npm (JS dependency manager ) if you do not have it

   2. use next command to install all dependencies
     > npm install

   3. run command to 'compile'/build frontend
    > npm run dev
    or
    > npm run build

    4. add  --watch in to "webpack --mode development" line in package.json
       if you want to rebuild automatically on every change

 ## Run instructions
 ### Start Stream listener
    > Part 1 – BE-Part Consume the expense events provided by the Cashcog Expense-API
    > application that take data from stream - CASHCOG_STREAM_URL = "https://cashcog.xcnt.io/stream"
    1. Here is where application located -
        > InterviewXCNTGmbH/cashcogstreamlistener/streamlistener.py

     which use given stream endpoint - CASHCOG_STREAM_URL = "https://cashcog.xcnt.io/stream"
      (this can be adjusted here - InterviewXCNTGmbH/app/config.py)

    2. use command
        > python InterviewXCNTGmbH/cashcogstreamlistener/streamlistener.py
      to run streamlistener in order to transfer data in to DB

    3. use clean DB script in case you want to start from scratch
       > python InterviewXCNTGmbH/cashcogstreamlistener/clear_all_db.py

### Start API application
    > Part 1 – BE-Part - RESTful-API which allows clients to fetch, update (approve or decline), and query these expenses.
    > api application that provide expenses interface (GET, POST,PUT) data

    1.  Here is where application located -
        > InterviewXCNTGmbH/app

    2. Run it with
       >  python InterviewXCNTGmbH/api/app_expenses_cashcog_xcnt.py

    3. application will be started on
            PORT_API_APP = "5001"
             SERVER_NAME_API_APP = "/cashcogXCNT/api/v1"
        > http://localhost:5001/cashcogXCNT/api/v1

         available methods you can found in InterviewXCNTGmbH/api/resources/expense.py
    It works as independent service with Flask ecosystem

 ### Start web application -
    > Part 2 – FE-Part Visualize the approval process in a web application.
    1.  Here is where application located -
        > InterviewXCNTGmbH/app

    2. Run it with
       >  python InterviewXCNTGmbH/app/app_expenses_cashcog_xcnt.py

    3. single page web application will be started on
            SERVER_NAME_WEB_APP = "/CashcogXCNT-Expenses"
            PORT_WEB_APP = "5000"
        > http://localhost:5000/CashcogXCNT-Expenses/

    4. To see DB data from stream

       > http://localhost:5000/CashcogXCNT-Expenses/#/expenses

    5. To see requests log data from DB use this page

       > http://localhost:5000/CashcogXCNT-Expenses/#/logs
