import os

SECRET_KEY = 'There-is-no-spoon'
DEBUG=True

DB_USERNAME='magal36'
DB_PASSWORD=''
BLOG_DATABASE_NAME='blog'

#cloud9 host config
DB_HOST=os.getenv('IP','0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
#SQLALCHEMY_DATABASE_URI = "sqlite:///home/ubuntu/workspace/blog.db"
SQLAlCHEMY_TRACK_MODIFICATIONS = True