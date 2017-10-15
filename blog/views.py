from my_blog import app
from my_blog import db, flush_obj, flush_commit
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

@app.route('/setup', methods=('GET','POST'))
def setup():
    form=SetupForm()
    error = None
    error2 = None #, blogs_from_author
    if form.validate_on_submit():
        author= Author(form.fullname.data,
        form.email.data,
        form.username.data,
        form.password.data,
        True
        )
        error = flush_obj(author)
        if error:
            db.session.rollback()
            db.session.close()
            flash("Error registering admin user")
            return render_template('blog/setup.html', form=form, error=error)
        else:
            blog = Blog(form.name.data, 
            author.id
            )
            #TODO: Create view with author's blog, verify if name matches one of them using
            #blogs_from_author = Blog.query.filter_by().join etc
            #Throw error if author have blog with same name, else continue
            # blogs_from_author = db.query.filter_by(admin=author.id)
            # for blg in blogs_from_author:
            #     if blg.name==blog.name:
            #         error2="Blog and user already exists"
            #         db.sesssion.rollback()
            #         db.session.close()
            #         flash(error2)
            #         return render_template('blog/setup.html', form=form, error=error2)                
            error2 = flush_commit(blog)
            if error2:
                flash("Unexpected Database Error registering Blog")
                return render_template('blog/setup.html', form=form, error=error2)
            else:
                flash("Blog created")
                return redirect(url_for('admin'))
    return render_template('blog/setup.html', form=form, error=error)