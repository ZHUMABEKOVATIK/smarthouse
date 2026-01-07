from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        print(f"{exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error."},
        )
