from fastapi import APIRouter
from .admin import router as admin_router
from .users import router as users_router

routers = APIRouter(prefix="/auth")

routers.include_router(admin_router)
routers.include_router(users_router)