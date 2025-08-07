from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.core.config import settings
from app.api.v1.endpoints import router

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, 
                  version=settings.VERSION, 
                  debug=settings.DEBUG)
    app.include_router(router, prefix=settings.API_PREFIX)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
    return app

app = create_app()

