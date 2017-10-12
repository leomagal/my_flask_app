Dropped all database: 

    $ python manage.py shell
    >>> from my_blog import db
    >>> from author.models import Author
    >>> db.drop_all()

Initizalized migrations dir:

    $ python manage.py db init
    