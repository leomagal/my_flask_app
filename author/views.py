from my_blog import app
from my_blog import db
from my_blog import flush_commit, flush_obj
from flask import render_template, redirect, url_for, flash, session, request
from sqlalchemy.exc import IntegrityError
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt


@app.route('/login', methods=('GET', 'POST'))
def login():
    form=LoginForm()
    error=None
    if request.method=='GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)
    if form.validate_on_submit():
        authors = Author.query.filter_by(
            username=form.username.data).limit(1)
        if authors.count():
            author = authors[0]
            if bcrypt.hashpw(form.password.data, author.password) == author.password:
                session['username'] = author.username
                if 'next' in session:
                    next= session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('login_success'))
            else:
                error="Invalid username or password"
        else:
            error="Invalid username or password"
    return render_template('author/login.html', form=form, error=error)
    
@app.route('/register', methods = ('GET', 'POST'))
def register():
    form = RegisterForm()
    error = None
    #get_flashed_messages()
    if form.validate_on_submit():
        author= Author(form.fullname.data,
        form.email.data,
        form.username.data,
        form.password.data,
        True
        )
        error = flush_commit(author)
        if error:
            return render_template('author/register.html', form=form, error=error)
        else:
            return redirect(url_for('success'))
    else:
        return render_template('author/register.html', form=form, error=error)

@app.route('/success')
def success():
    return "Author registration successfull"
    
@app.route('/login_success')
@login_required
def login_success():
    return "Author logged in"