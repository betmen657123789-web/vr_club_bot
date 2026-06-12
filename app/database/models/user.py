from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Integer
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    first_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    registered_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    last_activity: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    messages_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )