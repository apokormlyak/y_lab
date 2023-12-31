"""3  migration

Revision ID: 9c8ae41c92d7
Revises: d33c56c1afe5
Create Date: 2023-07-24 20:26:58.425649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c8ae41c92d7'
down_revision = 'd33c56c1afe5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_submenu_description', table_name='submenu')
    op.drop_index('ix_submenu_dish_id', table_name='submenu')
    op.drop_index('ix_submenu_menu_id', table_name='submenu')
    op.drop_index('ix_submenu_name', table_name='submenu')
    op.drop_table('submenu')
    op.drop_index('ix_menu_name', table_name='menu')
    op.drop_index('ix_menu_submenu_id', table_name='menu')
    op.drop_table('menu')
    op.drop_index('ix_dishes_description', table_name='dishes')
    op.drop_index('ix_dishes_name', table_name='dishes')
    op.drop_index('ix_dishes_price', table_name='dishes')
    op.drop_table('dishes')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dishes',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('dishes_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='dishes_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_dishes_price', 'dishes', ['price'], unique=False)
    op.create_index('ix_dishes_name', 'dishes', ['name'], unique=False)
    op.create_index('ix_dishes_description', 'dishes', ['description'], unique=False)
    op.create_table('menu',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('submenu_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['submenu_id'], ['submenu.id'], name='menu_submenu_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='menu_pkey')
    )
    op.create_index('ix_menu_submenu_id', 'menu', ['submenu_id'], unique=False)
    op.create_index('ix_menu_name', 'menu', ['name'], unique=False)
    op.create_table('submenu',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('menu_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('dish_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['dish_id'], ['dishes.id'], name='submenu_dish_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['menu_id'], ['submenu.id'], name='submenu_menu_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='submenu_pkey')
    )
    op.create_index('ix_submenu_name', 'submenu', ['name'], unique=False)
    op.create_index('ix_submenu_menu_id', 'submenu', ['menu_id'], unique=False)
    op.create_index('ix_submenu_dish_id', 'submenu', ['dish_id'], unique=False)
    op.create_index('ix_submenu_description', 'submenu', ['description'], unique=False)
    # ### end Alembic commands ###
