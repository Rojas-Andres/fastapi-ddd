from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.middleware import ErrorHandlerMiddleware  # noqa: E402
from app.infrastructure.api.routers import auth_router

app = FastAPI(title="FastAPI DDD Architecture", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ErrorHandlerMiddleware)
app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])


@app.get("/healtcheck/")
def api_healtcheck():
    return {"status": "ok"}
