import uvicorn
from fastapi import FastAPI

from .core import lifespan_setup, setup_cors, register_exception_handlers
from .api import routers

app = FastAPI(
    title="Smart House",
    lifespan=lifespan_setup,
    version="1.0.1"
)

setup_cors(app)
register_exception_handlers(app)


@app.get("/")
async def home():
    return "Developed at Bizler Group"

app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        port=8090
    )