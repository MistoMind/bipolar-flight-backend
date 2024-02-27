"""empty message

Revision ID: 9a6919682a0e
Revises: 94dc7605ab59
Create Date: 2024-02-27 00:37:16.210418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "9a6919682a0e"
down_revision: Union[str, None] = "94dc7605ab59"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    op.drop_table("flight")

    op.create_table(
        "flight",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("source", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("destination", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("dep_date", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column("departure", postgresql.TIME(), autoincrement=False, nullable=False),
        sa.Column("arrival", postgresql.TIME(), autoincrement=False, nullable=False),
        sa.Column(
            "price",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "seats", sa.INTEGER(), autoincrement=False, nullable=False, default=60
        ),
        sa.PrimaryKeyConstraint("id", name="flight_pkey"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "flight",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("source", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("destination", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("dep_date", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column("departure", postgresql.TIME(), autoincrement=False, nullable=False),
        sa.Column("arrival", postgresql.TIME(), autoincrement=False, nullable=False),
        sa.Column(
            "price",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="flight_pkey"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
    )
    # ### end Alembic commands ###