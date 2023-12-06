from app import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thread_id = db.Column(db.Integer)
    post_text = db.Column(db.String(1024))
    post_date = db.Column(db.DateTime)
    anon_tripcode = db.Column(db.Integer) # unique user tripcode

class Threads(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thread_id = db.Column(db.Integer, unique = True)
    count_of_posts = db.Column(db.Integer) # counting post, using for thread_bamping
    theme = db.Column(db.String(2)) # where thread must be
    thread_bamping = db.Column(db.Integer)  # if thread has more than 100 posts it will not get to the top of pages