from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

UPLOAD_FOLDER = '/home/tema/NG-ach/server_storage/images/'
#app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../../client/templates')) #creating flask app and choose folder for templates
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../../client/templates'), static_folder='/home/tema/NG-ach/server_storage', static_url_path='/server_storage')
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app) #creating database 
migrate = Migrate(app, db) # migrate using for upgrade database, like as adding new tables.

from app import routes, models, auth