"""Change tier to string type

Revision ID: a6eb6763c66d
Revises: da6d168caf67
Create Date: 2021-04-15 22:07:17.171079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6eb6763c66d'
down_revision = 'da6d168caf67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('raids', 'tier',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('raids', 'tier',
               existing_type=sa.String(length=50),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
