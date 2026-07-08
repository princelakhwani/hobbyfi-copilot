from fastapi import APIRouter, Depends

from app.database.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/trial")
def trial_users(
    sport: str,
    db=Depends(get_db),
):
    repository = UserRepository(db)
    service = UserService(repository)

    return service.trial_users(sport)