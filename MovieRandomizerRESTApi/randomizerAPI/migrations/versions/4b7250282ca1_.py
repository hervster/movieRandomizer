"""empty message

Revision ID: 4b7250282ca1
Revises: 
Create Date: 2020-07-20 23:41:56.600765

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4b7250282ca1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movieName', sa.String(), nullable=True),
    sa.Column('movieDirector', sa.String(), nullable=True),
    sa.Column('movieYear', sa.String(), nullable=True),
    sa.Column('allMovies', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
