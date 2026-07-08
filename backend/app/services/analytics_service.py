from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    def __init__(self, repository: AnalyticsRepository):
        self.repository = repository

    def revenue_today(self):

        revenue = self.repository.get_total_revenue()

        return {
            "revenue": revenue
        }