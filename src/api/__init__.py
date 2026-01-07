from fastapi import APIRouter
from src.api.v1 import routers as v1_routers

routers = APIRouter()

routers.include_router(v1_routers)