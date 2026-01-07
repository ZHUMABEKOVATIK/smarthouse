from fastapi import APIRouter, Depends, HTTPException

from src.database.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter(prefix="/city", tags=['API для создания город'])

@router.post("/")
async def add_city(
    session: AsyncSession = Depends(get_async_session)
):
    try:
        pass
    except Exception as err:
        pass