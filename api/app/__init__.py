from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),'../uploads/images') #where images would save
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'),static_folder=os.path.join(os.path.dirname(__file__),'../uploads'))
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app) #creating database 
migrate = Migrate(app, db) # migrate using for upgrade database, like as adding new tables.

from app import routes, models, auth