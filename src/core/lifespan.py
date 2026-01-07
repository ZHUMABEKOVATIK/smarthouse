from fastapi import FastAPI
from contextlib import asynccontextmanager

from database.database import async_main, engine

@asynccontextmanager
async def lifespan_setup(app: FastAPI):
    print("Start...")
    await async_main()
    yield
    await engine.dispose()
    print("End...")