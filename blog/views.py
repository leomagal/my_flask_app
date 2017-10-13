from my_blog import app
from my_blog import db
from flask import render_template, redirect, url_for, flash
from blog.form import SetupForm
from blog.models import Blog
from author.models import Author

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"
    
@app.route('/admin')
def admin():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return render_template('blog/admin.html')

@app.route('setup')
def setup():
    form=SetupForm
    return render_template('blog/setup.html')