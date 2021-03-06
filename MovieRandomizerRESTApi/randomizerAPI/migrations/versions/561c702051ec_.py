"""empty message

Revision ID: 561c702051ec
Revises: 4b7250282ca1
Create Date: 2020-07-21 11:56:35.593074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '561c702051ec'
down_revision = '4b7250282ca1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('dateWatched', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'dateWatched')
    # ### end Alembic commands ###
