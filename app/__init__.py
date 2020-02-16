"""
  standard Flask app setup
  application will run on default port with default prefix-  http://127.0.0.1:5000/
"""

from flask import Flask, Blueprint
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# setup flask application
app = Flask(__name__)
app_blueprint = Blueprint("blueprint_cashcog_react", __name__, template_folder='templates')

# add configuration to it
app.config.from_object(Config)
# app.config['APPLICATION_ROOT'] = Config.SERVER_NAME_WEB_APP

# add DB - just sqllite
db = SQLAlchemy(app)
migrate = Migrate(app, db)
marshmallow = Marshmallow(app)

from app import routes, models

