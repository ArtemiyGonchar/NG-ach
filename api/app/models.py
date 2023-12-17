from app import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thread_id = db.Column(db.Integer)
    post_text = db.Column(db.String(1024))
    post_date = db.Column(db.DateTime)
    image_name = db.Column(db.String(64))
class Threads(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thread_name = db.Column(db.String(64))
    theme = db.Column(db.String(2)) # where thread must be
    thread_text = db.Column(db.String(2064))

class Themes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    theme_name = db.Column(db.String(64), unique = True)
    theme_context = db.Column(db.String(256))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(256))