from fastapi import FastAPI

from smitepaper.api.wallpapers import wallpaper_router

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc")

app.include_router(wallpaper_router)
