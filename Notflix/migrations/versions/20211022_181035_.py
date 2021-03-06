"""empty message

Revision ID: c7f43e9cb9ea
Revises: f9eb5bccb8b5
Create Date: 2021-10-22 18:10:35.730559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7f43e9cb9ea'
down_revision = 'f9eb5bccb8b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_url', sa.String(length=2000), nullable=False),
    sa.Column('movie_thumbnail', sa.String(length=2000), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('year_released', sa.Integer(), nullable=False),
    sa.Column('production', sa.String(length=500), nullable=False),
    sa.Column('maturity_rating', sa.String(length=20), nullable=False),
    sa.Column('director', sa.String(length=500), nullable=False),
    sa.Column('cast', sa.String(length=500), nullable=False),
    sa.Column('run_time', sa.String(length=20), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('kids', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_genres',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'genre_id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('profile_img', sa.String(length=1000), nullable=True),
    sa.Column('kids', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'profile_id')
    )
    op.create_table('watchlist',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'profile_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watchlist')
    op.drop_table('likes')
    op.drop_table('profiles')
    op.drop_table('movie_genres')
    op.drop_table('movies')
    op.drop_table('genres')
    # ### end Alembic commands ###
