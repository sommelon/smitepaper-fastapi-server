from smitepaper.apps.core.routers import wallpapers


@wallpapers.get("/")
async def wallpapers():
    return {}
