"""empty message

Revision ID: bdd79a8686b8
Revises: bc561e86e2b4
Create Date: 2018-05-02 07:40:35.019682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdd79a8686b8'
down_revision = 'bc561e86e2b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('servidor', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'servidor', 'usuario', ['usuario_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'servidor', type_='foreignkey')
    op.drop_column('servidor', 'usuario_id')
    # ### end Alembic commands ###
