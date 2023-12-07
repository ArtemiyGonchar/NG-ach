from app import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thread_id = db.Column(db.Integer)
    post_text = db.Column(db.String(1024))
    post_date = db.Column(db.DateTime)

class Threads(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thread_id = db.Column(db.Integer, unique = True)
    thread_name = db.Column(db.String(64))
    count_of_posts = db.Column(db.Integer) # counting post, using for thread_bamping
    theme = db.Column(db.String(2)) # where thread must be
    thread_bamping = db.Column(db.Integer)  # if thread has more than 100 posts it will not get to the top of pages

class Themes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    theme_name = db.Column(db.String(64), unique = True)
    theme_context = db.Column(db.String(256))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(256))