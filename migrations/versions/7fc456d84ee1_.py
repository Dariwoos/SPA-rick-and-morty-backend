"""empty message

Revision ID: 7fc456d84ee1
Revises: 6a43b76ce394
Create Date: 2021-05-28 18:02:31.871614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fc456d84ee1'
down_revision = '6a43b76ce394'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('bank_account', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('bank_account', 'user', ['bank_account'], unique=False)
    # ### end Alembic commands ###
