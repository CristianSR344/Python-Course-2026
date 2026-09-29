from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=80)
    last_name: str = Field(min_length=1, max_length=80)
    email: EmailStr
    department: str = Field(min_length=1, max_length=100)
    role: str = Field(min_length=1, max_length=80)
    active: bool = True
    employee_id: str | None = Field(default=None, max_length=50)
    phone: str | None = Field(default=None, max_length=40)
    comments: str | None = Field(default=None, max_length=1000)

    @field_validator("first_name", "last_name", "department", "role")
    @classmethod
    def required_text(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be blank")
        return value.strip()

    @field_validator("employee_id", "phone", "comments")
    @classmethod
    def optional_text(cls, value: str | None) -> str | None:
        return value.strip() or None if value is not None else None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

