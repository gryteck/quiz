from datetime import datetime
import requests

from quiz.models import QuizQuestion
from config import settings


def post_unique_question(db, count):
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
        return [{'question': res['question'], 'answer': res['answer']} for res in questions]
