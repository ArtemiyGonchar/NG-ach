"""deleted id, count of posts

Revision ID: 4ce9a65db624
Revises: bd28c83cc0a3
Create Date: 2023-12-17 13:56:37.657994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ce9a65db624'
down_revision = 'bd28c83cc0a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('threads', schema=None) as batch_op:
        batch_op.drop_column('thread_id')
        batch_op.drop_column('thread_bamping')
        batch_op.drop_column('count_of_posts')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('threads', schema=None) as batch_op:
        batch_op.add_column(sa.Column('count_of_posts', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('thread_bamping', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('thread_id', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
