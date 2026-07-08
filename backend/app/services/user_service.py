from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def trial_users(self, sport: str):
        users = self.repository.get_trial_users(sport)

        return {
            "count": len(users),
            "users": [
                {
                    "name": user.name,
                    "email": user.email,
                    "trial_remaining": user.trial_remaining,
                }
                for user in users
            ],
        }