"""Added semester details

Revision ID: ef478711822e
Revises: d48640fdbd48
Create Date: 2024-04-05 20:53:18.924744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef478711822e'
down_revision = 'd48640fdbd48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('finals', sa.Column('semester', sa.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('finals', 'semester')
    # ### end Alembic commands ###