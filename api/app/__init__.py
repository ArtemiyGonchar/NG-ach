from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../../client/templates')) #creating flask app and choose folder for templates
app.config.from_object(Config)
db = SQLAlchemy(app) #creating database 
migrate = Migrate(app, db) # migrate using for upgrade database, like as adding new tables.

from app import routes, models, auth