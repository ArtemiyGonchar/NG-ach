from app import app, db
from flask import Flask, render_template, url_for, redirect, request, session
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Posts, Threads, Themes, Admin
from app.auth import auth, SECRET_KEY
import sqlalchemy

app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/debug-page') #page where we can debug or test new features
def debug_page():
    return render_template('test.html')

@app.route('/') # home page where you can choose your theme
def home_page():
    themeNames = []
    allThemes = Themes.query.all()
    for theme in allThemes:
        themeNames.append(theme.theme_name)
    admin_logged_in = session.get('admin_logged_in', False)
    return render_template('home.html', themes = themeNames, adminLogged = admin_logged_in)

@app.route('/<theme>')
def theme_page(theme):
    return render_template('themePage.html', theme_name = theme)
    
#-----------------------------ADMIN ROUTES-----------------------------#
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

@app.route('/remove-theme', methods = ['POST'])
@auth.login_required
def remove_theme():
    theme = request.form.get('remove')
    db.session.query(Themes).filter(Themes.theme_name == theme).delete()
    db.session.commit()
    return redirect('/')

@app.route('/admin-log')
@auth.login_required
def admin_log():
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect('/')


@app.route('/admin-reg', methods = ['POST'])
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


app.run(host='0.0.0.0', port=8080)