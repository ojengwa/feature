"""empty message

Revision ID: 7044d2465076
Revises: 
Create Date: 2018-11-14 01:10:33.897024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7044d2465076'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.Binary(), nullable=False),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('feature_requests',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('client', sa.Enum('client_one', 'client_two', 'client_three', name='clients'), nullable=False),
    sa.Column('client_priority', sa.Integer(), nullable=True),
    sa.Column('product_area', sa.Enum('policies', 'billing', 'claims', 'reports', name='productareas'), nullable=False),
    sa.Column('available_on', sa.DateTime(), nullable=True),
    sa.Column('requested_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['requested_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature_requests')
    op.drop_table('users')
    # ### end Alembic commands ###
