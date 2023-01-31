"""empty message

Revision ID: e6f04795bc28
Revises: 
Create Date: 2023-01-15 20:08:49.701627

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e6f04795bc28"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=64), nullable=True),
        sa.Column("last_name", sa.String(length=64), nullable=True),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("email", sa.String(length=128), nullable=True),
        sa.Column("password", sa.String(length=128), nullable=True),
        sa.Column("is_staff", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###