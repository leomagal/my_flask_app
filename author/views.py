from my_blog import app
from my_blog import db
from flask import render_template, redirect, url_for, flash
from author.form import RegisterForm
from author.models import Author

@app.route('/login')
def login():
    return "Login Successfull"
    
@app.route('/register', methods = ('GET', 'POST'))
def register():
    form = RegisterForm()
    error=None
    if form.validate_on_submit():
        author= Author(form.fullname.data,
        form.email.data,
        form.username.data,
        form.password.data,
        True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            db.session.commit()
            flash("Author registered")
            return redirect(url_for('success'))
    return render_template('author/register.html', form=form)

@app.route('/success')
def success():
    return "Author Registration Successfull"