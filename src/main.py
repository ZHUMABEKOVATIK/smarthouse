import uvicorn
from fastapi import FastAPI

from src.config import setup_cors, lifespan_setup

app = FastAPI(
    lifespan=lifespan_setup
)

setup_cors(
    app=app
)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        port=8090
    )