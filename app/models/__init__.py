"""
Data structures, used in project.

Add your new models here so Alembic could pick them up.

You may do changes in tables, then execute
`alembic revision --message="Your text" --autogenerate`
and alembic would generate new migration for you
in staff/alembic/versions folder.
"""

from .base import OrmBase, UUIDModel, TimestampModel
from .example import ExampleModel


__all__ = ["OrmBase", "UUIDModel", "TimestampModel", "ExampleModel"]
