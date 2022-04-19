from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from config import SQL_LOGIN

engine = create_engine(SQL_LOGIN)

SessionLocal = sessionmaker(engine)
Base = declarative_base()


@contextmanager
def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
