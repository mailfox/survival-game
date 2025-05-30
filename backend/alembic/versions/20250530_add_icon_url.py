# /home/mailfox/survival-game/backend/alembic/versions/20250530_add_icon_url.py
from alembic import op
import sqlalchemy as sa

revision = '8a9d0e3f4b2c'
down_revision = None  # Замени на ID последней миграции, если есть
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('items', sa.Column('icon_url', sa.String(), nullable=True))

def downgrade():
    op.drop_column('items', 'icon_url')