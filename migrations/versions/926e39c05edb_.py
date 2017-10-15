"""empty message

Revision ID: 926e39c05edb
Revises: 68e6b51936a9
Create Date: 2017-10-13 19:46:56.580179

"""

# revision identifiers, used by Alembic.
revision = '926e39c05edb'
down_revision = '68e6b51936a9'

from alembic import op
import sqlalchemy as sa
from my_blog import db

engine = db.engine
engine.echo=True

def upgrade():
    if not engine.dialect.has_table(engine, 'blog'): 
        op.create_table('blog',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=True),
        sa.Column('admin', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['admin'], ['author.id'], ),
        sa.PrimaryKeyConstraint('id')
        )


def downgrade():
    if engine.dialect.has_table(engine, 'blog'):
        op.drop_table('blog')
