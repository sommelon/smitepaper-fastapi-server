from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from smitepaper.config import settings

Base = declarative_base()
engine = create_engine(settings.dsn, echo=True)
