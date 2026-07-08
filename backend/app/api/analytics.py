from fastapi import APIRouter, Depends

from app.database.session import SessionLocal
from app.repositories.analytics_repository import AnalyticsRepository
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/revenue")
def revenue(db=Depends(get_db)):

    repository = AnalyticsRepository(db)

    service = AnalyticsService(repository)

    return service.revenue_today()