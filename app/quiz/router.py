from fastapi import APIRouter, BackgroundTasks, Depends

from .schemas import QuestionRequest
from database import get_db
from .crud import get_unique_question

router = APIRouter(prefix='/quiz', tags=['QUIZ'])


@router.post("/")
def get_quiz_question(request: QuestionRequest, db=Depends(get_db)):
    quiz_question = get_unique_question(db, request.questions_num)
    if quiz_question:
        return quiz_question
    else:
        return {}
