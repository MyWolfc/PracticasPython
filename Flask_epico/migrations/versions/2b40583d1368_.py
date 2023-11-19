"""empty message

Revision ID: 2b40583d1368
Revises: 
Create Date: 2023-11-09 09:24:12.121907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b40583d1368'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_images',
    sa.Column('id_images', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('data', sa.LargeBinary(), nullable=False),
    sa.Column('rendered_data', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id_images')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_images')
    op.drop_table('users')
    # ### end Alembic commands ###
