from flask import Flask, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from sqlalchemy.exc import IntegrityError

## Functions ##
def flush_commit(obj):
    error = flush_obj(obj)
    if error:
        return error
    else:
        try:
            db.session.commit()
            db.session.close()
            error=''
            print("\n ***\nSession Commited\n ***")
            flash("DB Commit Successfull")
            return error
        except:
            error = "Unexpected error at database session commit"
            flash(error)
            db.session.rollback()
            db.session.close()
            return error
    
def flush_obj(obj):
    error=''
    db.session.add(obj)
    try:
        db.session.flush()
        print("\n ***\nSession Flushed\n ***")
        if obj.id:
            error='' #just in case
            print("\n ***\nSession Flushed\n ***")
            flash("Session Flushed")
            return error
    
    except IntegrityError as e:
        error = "DB Error: "+str(e.args[0][1:27])+(" ")+str(e.args[0][30:34])
        if error == "DB Error: pymysql.err.IntegrityError 1062":
            print("\n\n*** %s ***\n\n"%error)
            #flash("Try different username or email")
            db.session.rollback()
            db.session.close()
            return error 
        else: 
            error = "Other Database IntegrityError: %s" % str(e.args)
            flash(error)
            db.session.rollback()
            db.session.close()
            return error
    except:
        error = "Unexpected Database Error"
        flash(error)
        db.session.rollback()
        db.session.close()
        return error


## Main ##
app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blog import views
from author import views