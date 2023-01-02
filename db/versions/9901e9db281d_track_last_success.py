"""track_last_success

Revision ID: 9901e9db281d
Revises: f11ddc61016b
Create Date: 2023-01-01 23:17:02.152590

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9901e9db281d"
down_revision = "f11ddc61016b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("instances", sa.Column("last_ingest_success", sa.String(), nullable=True))
    op.add_column("instances", sa.Column("first_ingest_success", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("instances", "first_ingest_success")
    op.drop_column("instances", "last_ingest_success")
    # ### end Alembic commands ###
