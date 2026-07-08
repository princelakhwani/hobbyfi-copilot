import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class Booking(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "bookings"

    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
    )

    booking_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    amount: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="BOOKED",
    )

    vendor: Mapped["Vendor"] = relationship(
        back_populates="bookings",
    )

    user: Mapped["User"] = relationship(
        back_populates="bookings",
    )

    payment: Mapped["Payment"] = relationship(
        back_populates="booking",
        uselist=False,
    )