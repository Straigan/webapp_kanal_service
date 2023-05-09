"""Add column hash in table Order

Revision ID: 4aaa9cf699c4
Revises: e9a20dac547b
Create Date: 2023-05-06 06:28:55.821247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aaa9cf699c4'
down_revision = 'e9a20dac547b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hash_line', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('hash_line')

    # ### end Alembic commands ###