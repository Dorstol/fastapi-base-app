from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api import router as api_router
from src.core.config import settings
from src.core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    # Shutdown
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(
    api_router,
    prefix=settings.api.prefix,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
