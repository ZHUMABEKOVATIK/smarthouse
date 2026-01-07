from fastapi import APIRouter
from src.api.v1 import routers as v1_routers
from src.api.v2 import routers as v2_routers

routers = APIRouter()

routers.include_router(v1_routers)
routers.include_router(v2_routers)