from fastapi import APIRouter

from . import city
from . import auth

routers = APIRouter(
    prefix="/v1"
)

routers.include_router(auth.routers)
routers.include_router(city.router)