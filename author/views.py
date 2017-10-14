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
        db.session.add(author)
        print("\n***Added user to db Session***\n")
        try:
            db.session.flush()
            print("\n ***\nSession Flushed\n ***")
            if author.id:
                db.session.commit()
                print("\n ***\nSession Commited\n ***")
                flash("Author registered")
                return redirect(url_for('success'))
        except IntegrityError as e:
            error = "DB Error: "+str(e.args[0][1:27])+(" ")+str(e.args[0][30:34])
            if error == "DB Error: pymysql.err.IntegrityError 1062":
                print("\n\n*** %s ***\n\n"%error)
                flash("Try different username or email")
                db.session.rollback()
                db.session.close()
                return render_template('author/register.html', form=form, error=error)
            else: 
                error = "Unexpected IntegrityError: %s" % str(e.args)
                flash(error)
                db.session.rollback()
                db.session.close()
                return render_template('author/register.html', form=form, error=error)
    else:
        return render_template('author/register.html', form=form, error=error)

@app.route('/success')
def success():
    return "Author Registration Successfull"