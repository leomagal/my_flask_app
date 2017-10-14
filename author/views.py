from my_blog import app
from my_blog import db
from flask import render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from author.form import RegisterForm
from author.models import Author

@app.route('/login')
def login():
    return "Login Successfull"
    
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
        print("\n***\n Forms validated, querying database \n***")
        error = flush_commit(author)
        if error:
            return render_template('author/register.html', form=form, error=error)
        else:
            return redirect(url_for('success'))
    else:
        return render_template('author/register.html', form=form, error=error)

@app.route('/success')
def success():
    return "Author Registration Successfull"