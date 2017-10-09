Tried 

$ python manage.py shell

    >>> from my_blog import db
    >>> from author.models import *
    >>> db.create_all()

but the changes doesn't reflect on the database cli