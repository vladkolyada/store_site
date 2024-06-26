"""empty message

Revision ID: 844e7ed1d3f1
Revises: 
Create Date: 2023-06-18 19:32:36.327985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844e7ed1d3f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=25), nullable=False),
    sa.Column('password_hash', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_image_name', sa.String(), nullable=True),
    sa.Column('product_type', sa.String(length=20), nullable=True),
    sa.Column('product_title', sa.String(length=150), nullable=True),
    sa.Column('product_description', sa.String(length=450), nullable=True),
    sa.Column('product_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_products_product_description'), ['product_description'], unique=False)
        batch_op.create_index(batch_op.f('ix_products_product_title'), ['product_title'], unique=True)
        batch_op.create_index(batch_op.f('ix_products_product_type'), ['product_type'], unique=False)

    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('keyboard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foreign_key', sa.Integer(), nullable=True),
    sa.Column('number_of_keyboard_buttons', sa.Integer(), nullable=True),
    sa.Column('connection', sa.String(length=50), nullable=True),
    sa.Column('producing_country', sa.String(length=50), nullable=True),
    sa.Column('color', sa.String(length=30), nullable=True),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('backlight_color', sa.String(length=50), nullable=True),
    sa.Column('keyboard_layout', sa.String(length=100), nullable=True),
    sa.Column('interface', sa.String(length=100), nullable=True),
    sa.Column('weight', sa.String(length=20), nullable=True),
    sa.Column('appointment', sa.String(length=100), nullable=True),
    sa.Column('cable_length', sa.String(length=20), nullable=True),
    sa.Column('dimensions', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['foreign_key'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('laptops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foreign_key', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=30), nullable=True),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('processor_specifications', sa.String(length=150), nullable=True),
    sa.Column('graphics_card_specifications', sa.String(length=250), nullable=True),
    sa.Column('ram_specifications', sa.String(length=200), nullable=True),
    sa.Column('memory_capacity_specifications', sa.String(length=250), nullable=True),
    sa.Column('display_characteristics', sa.String(length=200), nullable=True),
    sa.Column('producing_country', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['foreign_key'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mouse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foreign_key', sa.Integer(), nullable=True),
    sa.Column('connection', sa.String(length=50), nullable=True),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.Column('interface', sa.String(length=50), nullable=True),
    sa.Column('number_of_mouse_buttons', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=30), nullable=True),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('weight', sa.String(length=50), nullable=True),
    sa.Column('sensor_type', sa.String(length=60), nullable=True),
    sa.Column('additional_functions', sa.String(length=300), nullable=True),
    sa.Column('dimensions', sa.String(length=200), nullable=True),
    sa.Column('cable_length', sa.String(length=10), nullable=True),
    sa.Column('producing_country', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['foreign_key'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foreign_key', sa.Integer(), nullable=False),
    sa.Column('product_image_name', sa.String(), nullable=True),
    sa.Column('product_title', sa.String(length=150), nullable=True),
    sa.Column('product_price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['foreign_key'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_orders_product_image_name'), ['product_image_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_orders_product_title'), ['product_title'], unique=False)

    op.create_table('pcs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foreign_key', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=30), nullable=True),
    sa.Column('processor_specifications', sa.String(length=150), nullable=True),
    sa.Column('graphics_card_specifications', sa.String(length=250), nullable=True),
    sa.Column('ram_specifications', sa.String(length=200), nullable=True),
    sa.Column('number_of_ram_slots', sa.Integer(), nullable=True),
    sa.Column('specifications_motherboard', sa.String(length=200), nullable=True),
    sa.Column('memory_capacity_specifications', sa.String(length=250), nullable=True),
    sa.Column('cpu_cooling', sa.String(length=150), nullable=True),
    sa.Column('power_supply_specifications', sa.String(length=100), nullable=True),
    sa.Column('case_characteristics', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['foreign_key'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foreign_key', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('color', sa.String(length=30), nullable=True),
    sa.Column('communication_standard_or_internet', sa.String(length=150), nullable=True),
    sa.Column('display_characteristics', sa.String(length=200), nullable=True),
    sa.Column('sim_card_characteristics', sa.String(length=100), nullable=True),
    sa.Column('characteristics_memory_functions', sa.String(length=250), nullable=True),
    sa.Column('operating_system', sa.String(length=60), nullable=True),
    sa.Column('characteristics_of_the_front_camera', sa.String(length=200), nullable=True),
    sa.Column('processor_specifications', sa.String(length=150), nullable=True),
    sa.Column('characteristics_of_the_main_camera', sa.String(length=200), nullable=True),
    sa.Column('power_characteristics', sa.String(length=100), nullable=True),
    sa.Column('connectors', sa.String(length=150), nullable=True),
    sa.Column('navigation', sa.String(length=80), nullable=True),
    sa.Column('dimensions', sa.String(length=200), nullable=True),
    sa.Column('producing_country', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['foreign_key'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tablet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foreign_key', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=30), nullable=True),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('display_characteristics', sa.String(length=200), nullable=True),
    sa.Column('characteristics_memory_functions', sa.String(length=150), nullable=True),
    sa.Column('operating_system', sa.String(length=60), nullable=True),
    sa.Column('characteristics_of_the_front_camera', sa.String(length=200), nullable=True),
    sa.Column('processor_specifications', sa.String(length=150), nullable=True),
    sa.Column('characteristics_of_the_main_camera', sa.String(length=200), nullable=True),
    sa.Column('power_characteristics', sa.String(length=100), nullable=True),
    sa.Column('connectors', sa.String(length=150), nullable=True),
    sa.Column('navigation', sa.String(length=80), nullable=True),
    sa.Column('dimensions', sa.String(length=200), nullable=True),
    sa.Column('producing_country', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['foreign_key'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tablet')
    op.drop_table('phones')
    op.drop_table('pcs')
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_orders_product_title'))
        batch_op.drop_index(batch_op.f('ix_orders_product_image_name'))

    op.drop_table('orders')
    op.drop_table('mouse')
    op.drop_table('laptops')
    op.drop_table('keyboard')
    op.drop_table('users')
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_products_product_type'))
        batch_op.drop_index(batch_op.f('ix_products_product_title'))
        batch_op.drop_index(batch_op.f('ix_products_product_description'))

    op.drop_table('products')
    op.drop_table('admin_users')
    # ### end Alembic commands ###
