"""Initial migration

Revision ID: 4e7bf01f0e90
Revises: 
Create Date: 2025-01-03 00:08:05.716901

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4e7bf01f0e90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('user')
    # op.drop_table('orders')
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_index('barcode')

    op.drop_table('products')
    op.drop_table('notifications')
    op.drop_table('inventory')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('location', mysql.ENUM('manufacturing', 'warehouse', 'loading_area'), nullable=False),
    sa.Column('quantity', mysql.INTEGER(), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='inventory_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('notifications',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('message', mysql.TEXT(), nullable=False),
    sa.Column('is_read', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('products',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('barcode', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.create_index('barcode', ['barcode'], unique=True)

    op.create_table('orders',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('quantity', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='orders_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###