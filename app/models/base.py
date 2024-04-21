import sqlalchemy as sa
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
import uuid as uuid_pkg


class UUIDModel(SQLModel, abstract=True):
    uuid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class TimestampModel(SQLModel, abstract=True):
    created_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc),
    )
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc),
    )
