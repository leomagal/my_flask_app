from my_blog import db, settings

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(settings.AUTHOR_FULLNAME_STRING_LENGHT))
    email = db.Column(db.String(settings.AUTHOR_EMAIL_STRING_LENGHT), unique=True)
    username = db.Column(db.String(settings.AUTHOR_USERNAME_STRING_LENGHT), unique=True)
    password = db.Column(db.String(settings.AUTHOR_PASSWORD_STRING_LENGHT))
    is_author = db.Column(db.Boolean)
    
    def __init__(self, fullname, email, username, password, is_author=False):
        self.fullname=fullname
        self.email=email
        self.username=username
        self.password=password
        self.is_author=is_author
        
    def __repr__(self):
        return '<Author %r>' % self.username
        