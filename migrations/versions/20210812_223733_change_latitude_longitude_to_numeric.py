"""Change latitude/longitude to numeric

Revision ID: 264f5e6be566
Revises: a6eb6763c66d
Create Date: 2021-08-12 22:37:33.853881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '264f5e6be566'
down_revision = 'a6eb6763c66d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('gyms', 'latitude',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(),
               existing_nullable=False)
    op.alter_column('gyms', 'longitude',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('gyms', 'longitude',
               existing_type=sa.Numeric(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('gyms', 'latitude',
               existing_type=sa.Numeric(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###