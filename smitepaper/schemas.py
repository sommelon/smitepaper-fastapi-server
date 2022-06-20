from __future__ import annotations

from datetime import date

from pydantic import BaseModel, HttpUrl, constr


class TagBaseSchema(BaseModel):
    title: str | None


class TagCreateSchema(TagBaseSchema):
    pass


class TagSchema(TagBaseSchema):
    id: int

    class Config:
        orm_mode = True


class WallpaperBaseSchema(BaseModel):
    title: str | None
    image_link: HttpUrl | None
    size: constr(regex=r"^\d{1,4}x\d{1,4}$") | None
    slug: str | None
    release_date: date | None


class WallpaperCreateSchema(WallpaperBaseSchema):
    pass


class WallpaperSchema(WallpaperBaseSchema):
    id: int
    tags: list[TagSchema] = []

    class Config:
        orm_mode = True
