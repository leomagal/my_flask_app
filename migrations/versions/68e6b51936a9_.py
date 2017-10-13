"""db init in manager shell

Revision ID: 68e6b51936a9
Revises: 182802cfb60d
Create Date: 2017-10-12 23:49:02.920058

"""

# revision identifiers, used by Alembic.
revision = '68e6b51936a9'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
    try:
        op.drop_table('author')
    except:
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
    op.drop_table('author')
