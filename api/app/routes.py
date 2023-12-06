from app import app, db
from flask import Flask, render_template, url_for, redirect, request
from app.models import Posts, Threads, Themes

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
def add_theme():
    if request.method == 'POST': # when we submit name and context in addTheme.html, all sended information goes here and added to the DB
        themeName = request.form.get('themename')
        themeContext = request.form.get('themecontext')
        db.session.add(Themes(theme_name = themeName, theme_context = themeContext))
        db.session.commit()
        return redirect('/')
    return render_template('addTheme.html') #for first entering the page with method GET


@app.route('/get-themes')
def get_themes():
    pass

app.run(hots='0.0.0.0', port=8080)