"""Pydantic validation demonstration."""

from pydantic import BaseModel, EmailStr, Field, field_validator


class Registration(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    department: str = Field(min_length=1, max_length=80)
    age: int = Field(ge=18, le=120)

    @field_validator("name", "department")
    @classmethod
    def strip_text(cls, value: str) -> str:
        return value.strip()


if __name__ == "__main__":
    registration = Registration(name=" Ada ", email="ada@example.com",
                                department="Engineering", age=36)
    print(registration.model_dump())

