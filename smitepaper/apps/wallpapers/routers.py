from fastapi import APIRouter


wallpapers = APIRouter(prefix="/api/wallpapers")


@wallpapers.get("/")
async def wallpapers():
    return {}
