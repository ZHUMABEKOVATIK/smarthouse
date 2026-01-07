from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.core import handle_exceptions
from src.database.database import get_async_session
from src.models import City
from src.schemas.city import CreateCity, CityOut

router = APIRouter(prefix="/city", tags=['API для создания городов'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CityOut)
async def add_city(
    payload: CreateCity,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        data = City(name=payload.name.strip())
        session.add(data)
        await session.commit()
        return data
    except Exception as err:
        return await handle_exceptions(session, {}, err, "Error in City Post Endpoint")
    
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CityOut])
async def get_cities_list(session: AsyncSession = Depends(get_async_session)):
    data = (
        await session.execute(select(City))
    ).scalars().all()
    return data

@router.put("/{city_id}", status_code=status.HTTP_200_OK, response_model=CityOut)
async def update_city_data(
    city_id: int,
    payload: CreateCity,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        data = (
            await session.execute(select(City).where(City.id == city_id))
        ).scalar_one_or_none()

        if not data:
            raise HTTPException(404, "City not found!")
        
        data.name = payload.name.strip()
        await session.commit()
        return data
    except Exception as err:
        return await handle_exceptions(session, {}, err, "Error in City Post Endpoint")
    
@router.delete("/{city_id}", status_code=status.HTTP_200_OK, response_model=CityOut)
async def update_city_data(
    city_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        data = (
            await session.execute(select(City).where(City.id == city_id))
        ).scalar_one_or_none()

        if not data:
            raise HTTPException(404, "City not found!")
        
        session.delete(city_id)
        await session.commit()
        return data
    except Exception as err:
        return await handle_exceptions(session, {}, err, "Error in City Post Endpoint")