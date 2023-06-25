"""add ref image

Revision ID: 7e997b8e5ace
Revises: 22987be49ce7
Create Date: 2023-05-02 16:56:12.688207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e997b8e5ace'
down_revision = '22987be49ce7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'trees',
        sa.Column('c_picture', sa.String(2000))
    )


def downgrade() -> None:
    pass
