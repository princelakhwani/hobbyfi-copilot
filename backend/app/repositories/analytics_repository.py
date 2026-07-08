from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.payment import Payment


class AnalyticsRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_total_revenue(self):

        revenue = (
            self.db.query(
                func.coalesce(
                    func.sum(Payment.amount),
                    0
                )
            )
            .scalar()
        )

        return float(revenue)