from app.repositories.membership_repository import MembershipRepository


class MembershipService:

    def __init__(self, repository: MembershipRepository):
        self.repository = repository

    def extend(
        self,
        email: str,
        days: int,
    ):

        membership = self.repository.extend_membership(
            email=email,
            days=days,
        )

        if membership is None:
            return {
                "success": False,
                "message": "User or membership not found."
            }

        return {
            "success": True,
            "message": "Membership updated successfully.",
            "expiry_date": membership.expiry_date,
        }