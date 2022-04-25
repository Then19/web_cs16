from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import SQL_LOGIN

engine = create_engine(SQL_LOGIN, pool_recycle=3600)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
