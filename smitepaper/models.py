import enum

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from smitepaper.db import Base
from smitepaper.types import IntEnum


class God(Base):
    class AttackType(enum.IntEnum):
        BOTH = 1
        MELEE = 2
        RANGED = 3

    class PowerType(enum.IntEnum):
        MAGICAL = 1
        PHYSICAL = 2

    class ClassType(enum.IntEnum):
        ASSASSIN = 1
        GUARDIAN = 2
        HUNTER = 3
        MAGE = 4
        WARRIOR = 5

    class DifficultyType(enum.IntEnum):
        EASY = 1
        AVERAGE = 2
        HARD = 3
        VERY_HARD = 4

    __tablename__ = "gods"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    pantheon = Column(String(255), nullable=False)
    attack_type = Column(IntEnum(AttackType), nullable=False)
    power_type = Column(IntEnum(PowerType), nullable=False)
    class_type = Column(IntEnum(ClassType), nullable=False)
    difficulty = Column(IntEnum(DifficultyType), nullable=False)
    release_date = Column(Date)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)


class Wallpaper(Base):
    __tablename__ = "wallpapers"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    image_link = Column(String)
    size = Column(String(9))
    slug = Column(String(255))
    release_date = Column(Date)  # TODO: obtain release dates for skins
    tags = relationship(
        "Tag", secondary="WallpaperTag", cascade="all, delete", backref="wallpapers"
    )


class WallpaperTag(Base):
    __tablename__ = "wallpaper_tags"

    wallpaper_id = Column(ForeignKey(Wallpaper.id), primary_key=True)
    tag_id = Column(ForeignKey(Tag.id), primary_key=True)
