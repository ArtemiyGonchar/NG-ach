from app import app, db
from flask import Flask, render_template, url_for, redirect, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Posts, Threads, Themes, Admin
from app.auth import auth, SECRET_KEY
import sqlalchemy

#KEY = SECRET_KEY
ADMIN_AUTH = False



@app.route('/debug-page') #page where we can debug or test new features
def debug_page():
    return render_template('test.html')

@app.route('/') # home page where you can choose your theme
def home_page():
    themeNames = []
    allThemes = Themes.query.all()
    for theme in allThemes:
        themeNames.append(theme.theme_name)
    return render_template('home.html', themes = themeNames)


@app.route('/add-theme', methods = ['GET', 'POST']) #easy adding new theme system
@auth.login_required
def add_theme():
    if request.method == 'POST': # when we submit name and context in addTheme.html, all sended information goes here and added to the DB
        themeName = request.form.get('themename')
        themeContext = request.form.get('themecontext')
        db.session.add(Themes(theme_name = themeName, theme_context = themeContext))
        db.session.commit()
        return redirect('/')
    return render_template('addTheme.html') #for first entering the page with method GET


@app.route('/admin-reg', methods = ['GET', 'POST'])
def admin_reg():
    if request.method == 'POST':
        if request.form.get('secretkey') == SECRET_KEY:
            admin_name = request.form.get('username')
            admin_password = generate_password_hash(request.form.get('password'))
            db.session.add(Admin(username = admin_name, password = admin_password))
            db.session.commit()
            return "Successful registration"
        else:
            return "Permission denied"
    return render_template('reg.html')
app.run(hots='0.0.0.0', port=8080)