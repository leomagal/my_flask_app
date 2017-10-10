$ python manage.py shell

    >>> from my_blog import db
    >>> from author.models import *
    >>> db.create_all()

works now. found typo in constant DB_URI