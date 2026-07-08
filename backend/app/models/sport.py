from typing import List
import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class Sport(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "sports"

    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    vendor: Mapped["Vendor"] = relationship(
        back_populates="sports",
    )

    users: Mapped[List["User"]] = relationship(
        back_populates="sport",
    )