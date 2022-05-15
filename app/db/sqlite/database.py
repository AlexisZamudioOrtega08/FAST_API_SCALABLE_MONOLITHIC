from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"

engine_sqlite = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine_sqlite)
)
Base = declarative_base()
