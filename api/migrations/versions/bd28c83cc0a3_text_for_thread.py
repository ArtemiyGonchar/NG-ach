"""text for thread

Revision ID: bd28c83cc0a3
Revises: 835b4fa77f7a
Create Date: 2023-12-17 13:45:34.527325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd28c83cc0a3'
down_revision = '835b4fa77f7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('threads', schema=None) as batch_op:
        batch_op.add_column(sa.Column('thread_text', sa.String(length=2064), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('threads', schema=None) as batch_op:
        batch_op.drop_column('thread_text')

    # ### end Alembic commands ###
