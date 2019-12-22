# standard Flask app setup
# application will run on default port -  http://127.0.0.1:5001/
from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup flask application
app = Flask(__name__)
# add configuration to it
app.config.from_object(Config)
# add DB - just sqllite
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models