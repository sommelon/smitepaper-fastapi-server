from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from smitepaper.config import settings

engine = create_engine(settings.dsn, echo=True)
Base = declarative_base(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with SessionLocal() as session:
        yield session
