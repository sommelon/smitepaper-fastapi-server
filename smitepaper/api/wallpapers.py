from fastapi import APIRouter

wallpaper_router = APIRouter(prefix="/api/wallpapers")


@wallpaper_router.get("/")
async def wallpapers():
    return {}
