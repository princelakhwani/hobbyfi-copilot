from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class Vendor(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "vendors"

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    users: Mapped[List["User"]] = relationship(
        back_populates="vendor",
        cascade="all, delete-orphan",
    )

    sports: Mapped[List["Sport"]] = relationship(
        back_populates="vendor",
        cascade="all, delete-orphan",
    )

    bookings: Mapped[List["Booking"]] = relationship(
        back_populates="vendor",
    )

    audit_logs: Mapped[List["AuditLog"]] = relationship(
        back_populates="vendor",
    )