"""added wfa_file

Revision ID: 8d3ace135928
Revises: 2b3ff44fa98b
Create Date: 2019-01-02 22:20:02.330167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d3ace135928'
down_revision = '2b3ff44fa98b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidates', sa.Column('wfa_file', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('candidates', 'wfa_file')
    # ### end Alembic commands ###
