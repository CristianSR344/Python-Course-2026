from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .users import get_user_service
from ..services import UserService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request,
              service: UserService = Depends(get_user_service)) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request, name="index.html", context={"stats": service.dashboard()})

