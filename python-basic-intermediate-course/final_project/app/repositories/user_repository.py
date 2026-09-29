from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from ..models import User
from ..schemas import UserCreate, UserUpdate


class UserRepository:
    """Encapsulates every user database operation."""

    def __init__(self, session: Session):
        self.session = session

    def create(self, data: UserCreate) -> User:
        user = User(**data.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def list(self, search: str = "") -> list[User]:
        statement = select(User)
        if search.strip():
            pattern = f"%{search.strip()}%"
            statement = statement.where(or_(
                User.first_name.ilike(pattern), User.last_name.ilike(pattern),
                User.email.ilike(pattern), User.employee_id.ilike(pattern),
                User.department.ilike(pattern)))
        return list(self.session.scalars(statement.order_by(User.id.desc())))

    def update(self, user: User, data: UserUpdate) -> User:
        for field, value in data.model_dump().items():
            setattr(user, field, value)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()

    def dashboard_stats(self) -> dict[str, object]:
        total = self.session.scalar(select(func.count(User.id))) or 0
        active = self.session.scalar(select(func.count(User.id)).where(User.active.is_(True))) or 0
        departments = self.session.scalar(select(func.count(func.distinct(User.department)))) or 0
        recent = list(self.session.scalars(select(User).order_by(User.created_at.desc()).limit(5)))
        return {"total": total, "active": active, "inactive": total - active,
                "departments": departments, "recent": recent}

