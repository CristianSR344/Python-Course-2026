"""Run: uvicorn 02_fastapi_basics:app --reload"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Course User API")


class UserCreate(BaseModel):
    name: str
    email: EmailStr


users: list[dict[str, object]] = []


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "User API is running"}


@app.get("/users")
def list_users() -> list[dict[str, object]]:
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> dict[str, object]:
    user = {"id": len(users) + 1, **payload.model_dump(mode="json")}
    users.append(user)
    return user


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, object]:
    found = next((user for user in users if user["id"] == user_id), None)
    if not found:
        raise HTTPException(status_code=404, detail="User not found")
    return found

