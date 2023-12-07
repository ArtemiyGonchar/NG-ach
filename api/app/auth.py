from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Admin
import sqlalchemy

SECRET_KEY = 'NG-ach'

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    admin = Admin.query.filter_by(username=username).first()
    if admin and admin.username == username and check_password_hash(admin.password, password):
        return username