"""empty message

Revision ID: bfb856c82797
Revises: e92aada782df
Create Date: 2024-02-28 01:30:44.676966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'bfb856c82797'
down_revision: Union[str, None] = 'e92aada782df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    op.drop_table('ticket')
    op.drop_table('flight')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('flight',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('flight_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('source', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('destination', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('dep_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('departure', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('arrival', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('total_seats', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('available_seats', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='flight_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('ticket',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('booked_seats', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('flight_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.id'], name='ticket_flight_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='ticket_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='ticket_pkey')
    )
    op.create_table('admin',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='admin_pkey')
    )
    # ### end Alembic commands ###
