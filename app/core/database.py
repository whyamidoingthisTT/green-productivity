from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True,
    echo = True,
    pool_size = 5,
    max_overflow = 10,
    pool_recycle = 1800
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass




