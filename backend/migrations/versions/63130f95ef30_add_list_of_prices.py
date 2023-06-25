"""add list of prices

Revision ID: 63130f95ef30
Revises: 7e997b8e5ace
Create Date: 2023-05-06 12:19:14.501652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63130f95ef30'
down_revision = '7e997b8e5ace'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('listprices',
    sa.Column('indexTree', sa.String(), nullable=False),
    sa.Column('rangePrice', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('url_link', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['indexTree'], ['trees.indexTree'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('indexTree', 'rangePrice')
    )


def downgrade() -> None:
    pass
