"""empty message

Revision ID: 78f7ba88a81c
Revises: 8d605dfa9722
Create Date: 2023-01-22 20:03:43.358295

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "78f7ba88a81c"
down_revision = "8d605dfa9722"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "article_tag_association",
        sa.Column("article_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("article_tag_association")
    # ### end Alembic commands ###
