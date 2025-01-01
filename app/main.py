from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.middleware import ErrorHandlerMiddleware  # noqa: E402
from app.infrastructure.api.routers import (
    category_router,
    locations_router,
    reviews_router,
)

app = FastAPI(title="Aplicación My World", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ErrorHandlerMiddleware)
app.include_router(
    locations_router.router, prefix="/api/v1/locations", tags=["locations"]
)
app.include_router(category_router.router, prefix="/api/v1/category", tags=["category"])
app.include_router(reviews_router.router, prefix="/api/v1/reviews", tags=["review"])


@app.get("/healtcheck/")
def api_healtcheck():
    return {"status": "ok"}
