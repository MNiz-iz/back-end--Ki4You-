"""init_table

Revision ID: 22987be49ce7
Revises: 
Create Date: 2023-05-01 23:12:00.391559

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '22987be49ce7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('features',
    sa.Column('indexFeatures', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('desc', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('indexFeatures')
    )
    op.create_table('pollutions',
    sa.Column('indexPollution', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('pollution_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('desc', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('indexPollution')
    )
    op.create_table('trees',
    sa.Column('indexTree', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('another_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sci_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('family', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('size', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hieght', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hieght_max', sa.Integer(), nullable=False),
    sa.Column('nature', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('flower', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('leaf', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('note_nature', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('grow_rate', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('watering', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sunrise', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('soil', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('breed', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('additional_care', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('special_feature', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('url_picture', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('min_price', sa.Integer(), nullable=False),
    sa.Column('max_price', sa.Integer(), nullable=False),
    sa.Column('advice', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('auspicious', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('plant_detail', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('countLike', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('indexTree')
    )
    op.create_table('hasfeatures',
    sa.Column('indexTree', sa.String(), nullable=False),
    sa.Column('indexFeatures', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['indexFeatures'], ['features.indexFeatures'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['indexTree'], ['trees.indexTree'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('indexTree', 'indexFeatures')
    )
    op.create_table('purifies',
    sa.Column('indexTree', sa.String(), nullable=False),
    sa.Column('indexPollution', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['indexPollution'], ['pollutions.indexPollution'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['indexTree'], ['trees.indexTree'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('indexTree', 'indexPollution')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purifies')
    op.drop_table('hasfeatures')
    op.drop_table('trees')
    op.drop_table('pollutions')
    op.drop_table('features')
    # ### end Alembic commands ###
