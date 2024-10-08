"""Initial migration

Revision ID: fcbea3af4f34
Revises: 
Create Date: 2024-09-06 14:46:00.163307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcbea3af4f34'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('wpm', sa.Integer(), nullable=True),
    sa.Column('accuracy', sa.Double(), nullable=True),
    sa.Column('correct', sa.Integer(), nullable=True),
    sa.Column('incorrect', sa.Integer(), nullable=True),
    sa.Column('extra', sa.Integer(), nullable=True),
    sa.Column('missed', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scores_datetime'), 'scores', ['datetime'], unique=False)
    op.create_index(op.f('ix_scores_name'), 'scores', ['name'], unique=False)
    op.create_index(op.f('ix_scores_wpm'), 'scores', ['wpm'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_scores_wpm'), table_name='scores')
    op.drop_index(op.f('ix_scores_name'), table_name='scores')
    op.drop_index(op.f('ix_scores_datetime'), table_name='scores')
    op.drop_table('scores')
    # ### end Alembic commands ###
