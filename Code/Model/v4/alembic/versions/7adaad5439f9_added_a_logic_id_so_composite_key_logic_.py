"""added a logic id, so: composite key (logic_type and logic_id)

Revision ID: 7adaad5439f9
Revises: bee420876c22
Create Date: 2019-01-13 17:31:53.522310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7adaad5439f9'
down_revision = 'bee420876c22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logic_repos', sa.Column('logic_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logic_repos', 'logic_id')
    # ### end Alembic commands ###
