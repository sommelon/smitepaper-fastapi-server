from fastapi import FastAPI
from .apps.wallpapers.routers import wallpapers

app = FastAPI(docs_url="api/docs", redoc_url="api/redoc")

app.include_router(wallpapers)
