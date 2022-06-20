from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from smitepaper.db import get_session
from smitepaper.models import Tag
from smitepaper.schemas import TagCreateSchema, TagSchema

tag_router = APIRouter(prefix="/api/tags")


@tag_router.get("/", response_model=list[TagSchema])
def list_tags(session: Session = Depends(get_session)):
    return session.query(Tag).all()


@tag_router.post("/")
def create_tags(tag: TagCreateSchema, session: Session = Depends(get_session)):
    tag = Tag(**tag.dict())
    session.add(tag)
    session.commit()
    session.refresh(tag)
    return tag


@tag_router.get("/{tag_id}", response_model=TagSchema)
def retrieve_tag(tag_id: int, session: Session = Depends(get_session)):
    return session.query(Tag).filter(Tag.id == tag_id).one()
