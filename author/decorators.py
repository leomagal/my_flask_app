from functools import wraps
from flask import session, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("In decorated function")
        if session.get('username') is None:
            print("All the way in")
            return redirect(url_for('login', next=request.url))
        return f(*args,**kwargs)
    return decorated_function