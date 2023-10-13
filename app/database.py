from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

from config import settings


# Создание базовой модели для хранения вопроса
Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



