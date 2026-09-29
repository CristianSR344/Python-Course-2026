from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Query, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..config import get_settings
from ..database import get_db
from ..repositories import UserRepository
from ..schemas import UserCreate, UserRead, UserUpdate
from ..services import EmailService, UserService
from ..services.user_service import UserNotFoundError

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_user_service(session: Session = Depends(get_db)) -> UserService:
    return UserService(UserRepository(session), EmailService(get_settings()))


def _payload(first_name: str, last_name: str, email: str, department: str,
             role: str, active: bool, employee_id: str, phone: str,
             comments: str) -> dict[str, object]:
    return {"first_name": first_name, "last_name": last_name, "email": email,
            "department": department, "role": role, "active": active,
            "employee_id": employee_id, "phone": phone, "comments": comments}


FormText = Annotated[str, Form()]


@router.get("/users", response_class=HTMLResponse)
def users_page(request: Request, q: str = Query(default=""),
               service: UserService = Depends(get_user_service)) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="users.html",
                                      context={"users": service.list(q), "q": q})


@router.get("/users/new", response_class=HTMLResponse)
def new_user_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="user_form.html",
                                      context={"user": None, "error": None})


@router.post("/users", response_class=HTMLResponse)
def create_user_page(request: Request, first_name: FormText, last_name: FormText,
                     email: FormText, department: FormText, role: FormText,
                     active: Annotated[bool, Form()] = False,
                     employee_id: Annotated[str, Form()] = "",
                     phone: Annotated[str, Form()] = "",
                     comments: Annotated[str, Form()] = "",
                     service: UserService = Depends(get_user_service)) -> Response:
    raw = _payload(first_name, last_name, email, department, role, active,
                   employee_id, phone, comments)
    try:
        user = service.create(UserCreate.model_validate(raw))
    except (ValidationError, IntegrityError) as error:
        service.repository.session.rollback()
        return templates.TemplateResponse(request=request, name="user_form.html",
            context={"user": raw, "error": "Check required fields and unique email/employee ID."},
            status_code=422)
    return RedirectResponse(f"/users/{user.id}?created=1", status_code=303)


@router.get("/users/{user_id}", response_class=HTMLResponse)
def user_detail(request: Request, user_id: int, created: bool = False,
                service: UserService = Depends(get_user_service)) -> HTMLResponse:
    try:
        user = service.get(user_id)
    except UserNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    return templates.TemplateResponse(request=request, name="user_detail.html",
                                      context={"user": user, "created": created})


@router.get("/users/{user_id}/edit", response_class=HTMLResponse)
def edit_user_page(request: Request, user_id: int,
                   service: UserService = Depends(get_user_service)) -> HTMLResponse:
    try:
        user = service.get(user_id)
    except UserNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    return templates.TemplateResponse(request=request, name="user_form.html",
                                      context={"user": user, "error": None})


@router.post("/users/{user_id}/edit")
def edit_user(user_id: int, first_name: FormText, last_name: FormText,
              email: FormText, department: FormText, role: FormText,
              active: Annotated[bool, Form()] = False,
              employee_id: Annotated[str, Form()] = "",
              phone: Annotated[str, Form()] = "",
              comments: Annotated[str, Form()] = "",
              service: UserService = Depends(get_user_service)) -> RedirectResponse:
    try:
        data = UserUpdate.model_validate(_payload(first_name, last_name, email,
            department, role, active, employee_id, phone, comments))
        service.update(user_id, data)
    except UserNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    except (ValidationError, IntegrityError) as error:
        service.repository.session.rollback()
        raise HTTPException(422, "Invalid or duplicate user data") from error
    return RedirectResponse(f"/users/{user_id}", status_code=303)


@router.post("/users/{user_id}/delete")
def delete_user_page(user_id: int,
                     service: UserService = Depends(get_user_service)) -> RedirectResponse:
    try:
        service.delete(user_id)
    except UserNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    return RedirectResponse("/users", status_code=303)


@router.get("/api/users", response_model=list[UserRead])
def api_list_users(q: str = Query(default=""),
                   service: UserService = Depends(get_user_service)) -> list:
    return service.list(q)


@router.get("/api/users/{user_id}", response_model=UserRead)
def api_get_user(user_id: int,
                 service: UserService = Depends(get_user_service)):
    try:
        return service.get(user_id)
    except UserNotFoundError as error:
        raise HTTPException(404, str(error)) from error


@router.post("/api/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def api_create_user(data: UserCreate,
                    service: UserService = Depends(get_user_service)):
    try:
        return service.create(data)
    except IntegrityError as error:
        service.repository.session.rollback()
        raise HTTPException(409, "Email or employee ID already exists") from error


@router.put("/api/users/{user_id}", response_model=UserRead)
def api_update_user(user_id: int, data: UserUpdate,
                    service: UserService = Depends(get_user_service)):
    try:
        return service.update(user_id, data)
    except UserNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    except IntegrityError as error:
        service.repository.session.rollback()
        raise HTTPException(409, "Email or employee ID already exists") from error


@router.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def api_delete_user(user_id: int,
                    service: UserService = Depends(get_user_service)) -> Response:
    try:
        service.delete(user_id)
    except UserNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    return Response(status_code=status.HTTP_204_NO_CONTENT)

