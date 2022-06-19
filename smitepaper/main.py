from fastapi import FastAPI

from smitepaper.routers import wallpapers

if __name__ == "__main__":
    app = FastAPI(docs_url="api/docs", redoc_url="api/redoc")

    app.include_router(wallpapers)
