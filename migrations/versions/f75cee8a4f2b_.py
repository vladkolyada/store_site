"""empty message

Revision ID: f75cee8a4f2b
Revises: 1f26a3002a3e
Create Date: 2023-06-11 12:25:35.559100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f75cee8a4f2b'
down_revision = '1f26a3002a3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('phones', schema=None) as batch_op:
        batch_op.alter_column('characteristics_memory_functions',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=250),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('phones', schema=None) as batch_op:
        batch_op.alter_column('characteristics_memory_functions',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)

    # ### end Alembic commands ###
