from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.database.session import SessionLocal
from app.repositories.membership_repository import MembershipRepository
from app.services.membership_service import MembershipService

router = APIRouter(
    prefix="/membership",
    tags=["Membership"],
)


class ExtendRequest(BaseModel):
    email: str
    days: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/extend")
def extend_membership(
    request: ExtendRequest,
    db=Depends(get_db),
):

    repository = MembershipRepository(db)

    service = MembershipService(repository)

    return service.extend(
        request.email,
        request.days,
    )