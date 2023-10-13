from database import Base, engine
from sqlalchemy import Column, Integer, String, DateTime


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)


Base.metadata.create_all(bind=engine)

