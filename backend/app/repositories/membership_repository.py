from datetime import timedelta
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.membership import Membership


class MembershipRepository:

    def __init__(self, db: Session):
        self.db = db

    def extend_membership(
        self,
        email: str,
        days: int,
    ):

        user = (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

        if user is None:
            return None

        membership = (
            self.db.query(Membership)
            .filter(Membership.user_id == user.id)
            .first()
        )

        if membership is None:
            return None

        membership.expiry_date += timedelta(days=days)

        self.db.commit()
        self.db.refresh(membership)

        return membership