from app import app, db
from flask import Flask, render_template, url_for, redirect, request, session
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from app.models import Posts, Threads, Themes, Admin
from app.auth import auth, SECRET_KEY
import sqlalchemy
import os, datetime


app.config['SECRET_KEY'] = '/aGna2&*fg.gdg/edfGHJN3jk$*#kgjfA'
filename_list = os.listdir(app.config['UPLOAD_FOLDER'])
print(filename_list)
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

    threads = Threads.query.filter_by(theme = theme)
    thread_test = Threads.query.filter_by(theme = theme).first()
    if thread_test is None:
        return "Acces denied"
    admin_logged_in = session.get('admin_logged_in', False)
    return render_template('themePage.html', theme_name = theme, thread= threads, adminLogged = admin_logged_in, theme_context = Themes.query.filter_by(theme_name = theme).first())


@app.route('/<theme>/<thread>', methods = ['GET', 'POST'])
def thread_page(theme, thread):
    print(theme, thread)
    thread_data = Threads.query.filter_by(theme=theme, thread_name=thread).first()
    if thread_data is None:
        return "Acces denied"
    
    if request.method == 'POST':
        threadId = thread_data.id
        postText = request.form.get('posttext')
        postDate = datetime.datetime.now()
        if 'file' in request.files:
            file = request.files['file']
            filename = secure_filename(file.filename)
            if len(filename) != 0:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        db.session.add(Posts(post_text = postText, post_date = postDate, thread_id = threadId, image_name = filename))
        db.session.commit()
    posts = Posts.query.filter_by(thread_id = thread_data.id)
    return render_template('threadPage.html', thread = thread, thread_content = thread_data, theme = theme, posts = posts)


@app.route('/create-thread', methods = ['POST'])
def create_thread():
    if request.method == 'POST':
        threadname = request.form.get('threadname')
        threadtext = request.form.get('threadtext')
        themeforthread = request.form.get('theme')
        db.session.add(Threads(thread_name = threadname, thread_text = threadtext, theme = themeforthread))
        db.session.commit()
        return redirect ('/{}'.format(themeforthread))



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


@app.route('/remove-thread', methods = ['POST'])
@auth.login_required
def remove_thread():
    thread_id = request.form.get('remove')admin-reg
    Posts.query.filter_by(thread_id= thread_id).delete()
    Threads.query.filter_by(id=thread_id).delete()
    db.session.commit()
    return redirect('/')


@app.route('/remove-theme', methods = ['POST'])
@auth.login_required
def remove_theme():
    theme = request.form.get('remove')
    threads_delete = Threads.query.filter_by(theme=theme).all()
    for thread in threads_delete:
        Posts.query.filter_by(thread_id = thread.id).delete()
    Threads.query.filter_by(theme = theme).delete()
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


@app.route('/admin-reg', methods = ['POST', 'GET'])
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