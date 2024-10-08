"""payment table added

Revision ID: 6ee15708d5c4
Revises: 
Create Date: 2024-07-16 16:36:53.978454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ee15708d5c4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('payment_id', sa.String(length=50), nullable=False),
    sa.Column('Booking_id', sa.String(length=50), nullable=True),
    sa.Column('payment_method', sa.String(length=30), nullable=False),
    sa.Column('transaction_status', sa.String(length=30), nullable=False),
    sa.Column('total_amount', sa.String(length=20), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['Booking_id'], ['booking.id'], ),
    sa.PrimaryKeyConstraint('payment_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    # ### end Alembic commands ###
