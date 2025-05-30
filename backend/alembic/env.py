# /home/mailfox/survival-game/backend/alembic/env.py
import sys
import os

# Вычисляем корень проекта (backend)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
print(f"sys.path: {sys.path}")  # Отладочный вывод

from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from sqlalchemy.orm import declarative_base

Base = declarative_base()

config = context.config

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

try:
    from models.item import ItemDB
    from models.player import PlayerDB  # Исправлено с ItemDB на PlayerDB
    print("Successfully imported ItemDB and PlayerDB")
except ImportError as e:
    print(f"Error importing models: {e}")
    raise

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()