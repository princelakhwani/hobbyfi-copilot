import uuid

from sqlalchemy import ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class AuditLog(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "audit_logs"

    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
    )

    action: Mapped[str]

    old_value: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )

    new_value: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )

    vendor: Mapped["Vendor"] = relationship(
        back_populates="audit_logs",
    )