import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.config import Settings  # noqa: E402
from app.database import Base  # noqa: E402
from app.main import app  # noqa: E402
from app.repositories import UserRepository  # noqa: E402
from app.routers.users import get_user_service  # noqa: E402
from app.services import EmailService, UserService  # noqa: E402


@pytest.fixture
def client(tmp_path: Path):
    engine = create_engine(
        f"sqlite:///{tmp_path / 'test.db'}", connect_args={"check_same_thread": False})
    testing_session = sessionmaker(bind=engine, expire_on_commit=False)
    Base.metadata.create_all(engine)
    email_settings = Settings(email_log_dir=tmp_path / "emails", _env_file=None)

    def service_override():
        with testing_session() as session:
            yield UserService(UserRepository(session), EmailService(email_settings))

    app.dependency_overrides[get_user_service] = service_override
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(engine)
    engine.dispose()

