"""empty message

Revision ID: 192858f065d2
Revises: 
Create Date: 2023-05-31 13:12:17.771489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '192858f065d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('laptops')
    op.drop_table('products')
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_admin_username'))

    op.drop_table('admin')
    # ### end Alembic commands ###
