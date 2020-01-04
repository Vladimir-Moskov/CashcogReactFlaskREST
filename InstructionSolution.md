npm i -D webpack webpack webpack-cli
npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties
npm i react react-dom prop-types
npm i react-router-dom

npm run dev
npm run build
npm i axios react-alert  react-redux react-router-dom redux redux-devtools-extension redux-thunk

--watch

style="background-color: #e3f2fd;"


# flask db migrate -m "ApplicationRequestLog table"
# TODO: add better exception handling
http://127.0.0.1:5000/cashcogXCNT/api/v1/expense/1

5. TODO: fix time zone

# Here is solution
  1. Flask ecosystem has been used to implement task
  2. SQLAlchemy and ORM to deal with data model
  3. flask_migrate Migrate to manage DB changes(add/update/delete table/field/model)
  4. web application page mapping in app/routes
  5. batch job has been implemented as independent part of the system - here batch/steel_processing_batch.py


## Project repository
> https://github.com/Vladimir-Moskov/InterviewSmartSteelTechnologiesGmbH

## From point of view MVP (Minimum Valuable Product)

1. For simplicity - logging has not been added
> TODO: add real life logging
> https://www.scalyr.com/blog/getting-started-quickly-with-flask-logging/
> https://stackoverflow.com/questions/52728928/setting-up-a-database-handler-for-flask-logger

2. For simplicity - unit tests and integration tests has not been implemented as well
> TODO: add real life tests with pytest

3. For simplicity - there is no any authorization/security
> TODO: implement it

4. TODO: add flask-serialize

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
    > cd   your_local_folder/InterviewSmartSteelTechnologiesGmbH

 6. Run next command in order to create virtualenv for project
   > virtualenv venv

 7. Activate virtual environment
   > your_local_folder/InterviewSmartSteelTechnologiesGmbH/venv/Scripts/activate

 8. install project dependencies

   > pip install -r ../../requirements.txt

    and use

    > pip freeze > ../../requirements.txt

    in order to update list of project libraries
    and use

    > pip install <package-name>

    in case you miss some

 9. You do not need to setup/update DB - it has been added in to repository
   > Data Base: sql lite in file InterviewSmartSteelTechnologiesGmbH/app/app.db
   Here are some commands how to dial with it in case you want to do modifications
    > flask db init

    > flask db migrate -m "ApplicationRequestLog table"
    > flask db migrate -m "Expense table"
    > flask db migrate -m "Employee table"

    > flask db migrate

    > flask db upgrade

 10.

 ## Run instructions
 ### Start data extractor
    > application that transfers `task_data.csv` to a database
    1. Here is where application located -
        > InterviewSmartSteelTechnologiesGmbH/batch/steel_processing_batch.py

     which use given file `task_data.csv` from folder
      > InterviewSmartSteelTechnologiesGmbH/resource
      (this can be adjusted here - InterviewSmartSteelTechnologiesGmbH/app/config.py)

    2. use command
        > python InterviewSmartSteelTechnologiesGmbH/batch/steel_processing_batch.py
      to run data transfer in to DB

    3. use clean DB script in case you want to repeat a test
       > python InterviewSmartSteelTechnologiesGmbH/batch/clear_all_db.py

 ### Start web application
    > web application that is able to connect to this database

    1.  Here is where application located -
        > InterviewSmartSteelTechnologiesGmbH/app

    2. Run it with
       >  python InterviewSmartSteelTechnologiesGmbH/app/smart_steel_technologies.py

    3. application will be started on

        > http://localhost:5000/

        with home page

        > http://localhost:5000/index

    4. To see DB data from file `task_data.csv` use this page

       > http://localhost:5000/steelProcessing

    5. To see log data from DB use this page

       > http://localhost:5000/log
