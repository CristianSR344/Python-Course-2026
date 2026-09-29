from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
import re
import smtplib

from ..config import Settings


class EmailService:
    """Send SMTP mail when configured, otherwise write a development email file."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def _write_fallback(self, recipient: str, subject: str, body: str,
                        reason: str = "development mode") -> Path:
        directory = self.settings.email_log_dir
        directory.mkdir(parents=True, exist_ok=True)
        safe_recipient = re.sub(r"[^a-zA-Z0-9_.-]", "_", recipient)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        path = directory / f"{stamp}_{safe_recipient}.txt"
        path.write_text(
            f"Delivery: simulated ({reason})\nTo: {recipient}\nFrom: "
            f"{self.settings.smtp_from}\nSubject: {subject}\n\n{body}\n",
            encoding="utf-8")
        return path

    def send(self, recipient: str, subject: str, body: str) -> str:
        configured = all((self.settings.smtp_host, self.settings.smtp_user,
                          self.settings.smtp_password, self.settings.smtp_from))
        if not configured:
            path = self._write_fallback(recipient, subject, body)
            return f"simulated:{path}"
        message = EmailMessage()
        message["To"], message["From"], message["Subject"] = (
            recipient, self.settings.smtp_from, subject)
        message.set_content(body)
        try:
            with smtplib.SMTP(self.settings.smtp_host, self.settings.smtp_port,
                              timeout=10) as smtp:
                if self.settings.smtp_use_tls:
                    smtp.starttls()
                smtp.login(self.settings.smtp_user, self.settings.smtp_password)
                smtp.send_message(message)
            return "sent"
        except (OSError, smtplib.SMTPException) as error:
            path = self._write_fallback(recipient, subject, body,
                                        reason=f"SMTP error: {type(error).__name__}")
            return f"fallback:{path}"

