from pathlib import Path

from app.config import Settings
from app.services import EmailService


def test_email_falls_back_to_file(tmp_path: Path):
    service = EmailService(Settings(email_log_dir=tmp_path, _env_file=None))
    result = service.send("student@example.com", "Welcome", "Hello student")
    assert result.startswith("simulated:")
    files = list(tmp_path.glob("*.txt"))
    assert len(files) == 1
    content = files[0].read_text(encoding="utf-8")
    assert "student@example.com" in content
    assert "Hello student" in content

