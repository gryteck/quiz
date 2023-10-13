from fastapi import APIRouter, BackgroundTasks, Depends

from .crud import post_unique_question
from database import get_db
from .schemas import QuestionRequest

router = APIRouter(prefix='/quiz', tags=['QUIZ'])


@router.post("")
def get_quiz_question(request: QuestionRequest, db=Depends(get_db)):
    quiz_question = post_unique_question(db, request.questions_num)
    if quiz_question:
        return quiz_question
    else:
        return {}
