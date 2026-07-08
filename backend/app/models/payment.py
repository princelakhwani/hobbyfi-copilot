import uuid

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class Payment(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "payments"

    booking_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("bookings.id"),
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    payment_method: Mapped[str] = mapped_column(
        String(30),
        default="UPI",
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="SUCCESS",
    )

    booking: Mapped["Booking"] = relationship(
        back_populates="payment",
    )