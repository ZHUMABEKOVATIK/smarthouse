import uvicorn
from fastapi import FastAPI

from src.core import lifespan_setup, setup_cors, register_exception_handlers
from src.api import routers

app = FastAPI(
    title="Smart House",
    lifespan=lifespan_setup,
    version="1.0.1"
)

setup_cors(app)
register_exception_handlers(app)

app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        port=8090
    )