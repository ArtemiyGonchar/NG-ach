from app import app, db
from flask import Flask, render_template, url_for, redirect
from app.models import Posts, Threads

@app.route('/debug-page') #page where we can debug or test new features
def debug_page():
    return render_template('debugPage.html')

app.run(hots='0.0.0.0', port=8080)