from fastapi import FastAPI, Depends
from pydantic import BaseModel
import requests
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Создание базовой модели для хранения вопроса
Base = declarative_base()


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)


class QuestionRequest(BaseModel):
    questions_num: int


sqlite_url = 'sqlite:///quiz.sql'
pgsql_url = 'postgresql://postgres:test@localhost:5432/postgres'
docker_pgsql_url = 'postgresql://admin:test@postgres:5432/quiz'
engine = create_engine(docker_pgsql_url)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_unique_question(db, count):
    while True:
        response = requests.get(f"https://jservice.io/api/random?count={count}")
        if response.status_code == 200:
            questions = response.json()
            for question in questions:
                existing_question = db.query(QuizQuestion).filter_by(question=question["question"]).first()
                if existing_question is None:
                    quiz_question = QuizQuestion(
                        question=question["question"],
                        answer=question["answer"],
                        created_at=datetime.now()
                    )
                    db.add(quiz_question)
                    db.commit()
            return questions


@app.post("/quiz")
def get_quiz_question(request: QuestionRequest, db=Depends(get_db)):
    quiz_question = get_unique_question(db, request.questions_num)
    if quiz_question:
        return quiz_question
    else:
        return {}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
