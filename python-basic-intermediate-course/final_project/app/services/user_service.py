import logging

from ..models import User
from ..repositories import UserRepository
from ..schemas import UserCreate, UserUpdate
from .email_service import EmailService

logger = logging.getLogger(__name__)


class UserNotFoundError(LookupError):
    pass


class UserService:
    def __init__(self, repository: UserRepository, email_service: EmailService):
        self.repository = repository
        self.email_service = email_service

    def create(self, data: UserCreate, send_welcome: bool = True) -> User:
        user = self.repository.create(data)
        if send_welcome:
            result = self.email_service.send(
                user.email, "Welcome to the User Portal",
                f"Hello {user.first_name},\n\nYour user registration is complete.")
            logger.info("Welcome email for user %s: %s", user.id, result)
        return user

    def get(self, user_id: int) -> User:
        user = self.repository.get(user_id)
        if user is None:
            raise UserNotFoundError(f"User {user_id} not found")
        return user

    def list(self, search: str = "") -> list[User]:
        return self.repository.list(search)

    def update(self, user_id: int, data: UserUpdate) -> User:
        return self.repository.update(self.get(user_id), data)

    def delete(self, user_id: int) -> None:
        self.repository.delete(self.get(user_id))

    def dashboard(self) -> dict[str, object]:
        return self.repository.dashboard_stats()

