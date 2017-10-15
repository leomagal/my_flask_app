"""db init in manager shell

Revision ID: 68e6b51936a9
Revises: 182802cfb60d
Create Date: 2017-10-12 23:49:02.920058

"""

# revision identifiers, used by Alembic.
revision = '68e6b51936a9'
down_revision = None

from alembic import op
from my_blog import db
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

engine = db.engine
engine.echo=True

def upgrade():

    if not engine.dialect.has_table(engine, 'author'):
        op.create_table('author',
        sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
        sa.Column('fullname', mysql.VARCHAR(length=80), nullable=False),
        sa.Column('email', mysql.VARCHAR(length=35), nullable=False, unique=True),
        sa.Column('username', mysql.VARCHAR(length=80), nullable=False, unique=True),
        sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
        sa.Column('is_author', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='latin1',
        mysql_engine='InnoDB'
        )


def downgrade():
    if engine.dialect.has_table(engine, 'author'):
        op.drop_table('author')