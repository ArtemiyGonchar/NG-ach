"""added table Themes, it will be storage for theme names and its context.

Revision ID: 68b49c1612ba
Revises: 0a86620abb64
Create Date: 2023-12-06 19:22:36.540650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68b49c1612ba'
down_revision = '0a86620abb64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('themes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theme_name', sa.String(length=64), nullable=True),
    sa.Column('theme_context', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('theme_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('themes')
    # ### end Alembic commands ###