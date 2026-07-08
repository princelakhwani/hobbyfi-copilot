from sqlalchemy.orm import Session

from app.models.user import User
from app.models.sport import Sport


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_trial_users(self, sport_name: str):
        return (
            self.db.query(User)
            .join(Sport)
            .filter(
                Sport.name.ilike(sport_name),
                User.trial_remaining > 0,
            )
            .all()
        )