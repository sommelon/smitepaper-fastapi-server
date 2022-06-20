from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from smitepaper.db import get_session
from smitepaper.models import Tag, Wallpaper, WallpaperTag
from smitepaper.schemas import TagCreateSchema, WallpaperCreateSchema, WallpaperSchema

wallpaper_router = APIRouter(prefix="/api/wallpapers")


@wallpaper_router.get("/", response_model=list[WallpaperSchema])
def list_wallpapers(session: Session = Depends(get_session)):
    return session.query(Wallpaper).all()


@wallpaper_router.post("/")
def create_wallpapers(
    wallpaper: WallpaperCreateSchema, session: Session = Depends(get_session)
):
    wallpaper = Wallpaper(**wallpaper.dict())
    session.add(wallpaper)
    session.commit()
    session.refresh(wallpaper)
    return wallpaper


@wallpaper_router.get("/{wallpaper_id}", response_model=WallpaperSchema)
def retrieve_wallpaper(wallpaper_id: int, session: Session = Depends(get_session)):
    return session.query(Wallpaper).filter(Wallpaper.id == wallpaper_id).one()


@wallpaper_router.post("/{wallpaper_id}/tags", response_model=WallpaperSchema)
def create_wallpaper_tag(
    wallpaper_id: int, tag: TagCreateSchema, session: Session = Depends(get_session)
):
    tag = Tag(**tag.dict())
    wallpaper: Wallpaper = (
        session.query(Wallpaper).filter(Wallpaper.id == wallpaper_id).one()
    )
    wallpaper.tags.append(tag)
    session.commit()
    return wallpaper


@wallpaper_router.post("/{wallpaper_id}/tags/{tag_id}", response_model=WallpaperSchema)
def add_wallpaper_tag(
    wallpaper_id: int, tag_id: int, session: Session = Depends(get_session)
):
    wallpaper: Wallpaper = (
        session.query(Wallpaper).filter(Wallpaper.id == wallpaper_id).one()
    )
    tag: Tag = session.query(Tag).filter(Tag.id == tag_id).one()
    wallpaper.tags.append(tag)
    session.commit()
    return wallpaper


@wallpaper_router.delete("/{wallpaper_id}/tags/{tag_id}", status_code=204)
def remove_wallpaper_tag(
    wallpaper_id: int, tag_id: int, session: Session = Depends(get_session)
):
    # wallpaper: Wallpaper = (
    #     session.query(Wallpaper).filter(Wallpaper.id == wallpaper_id).one()
    # )
    session.query(WallpaperTag).filter(
        WallpaperTag.tag_id == tag_id, WallpaperTag.wallpaper_id == wallpaper_id
    ).delete()
    # wallpaper.tags.append(tag)
    session.commit()
    # return JSONResponse({})
