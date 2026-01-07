from fastapi import APIRouter

from . import city

routers = APIRouter(
    prefix="/v1"
)

routers.include_router(city.router)