from sqlalchemy import create_engine
from pydantic import BaseModel


class QuestionRequest(BaseModel):
    questions_num: int


engine = create_engine('postgresql://admin:test@postgres:5432/quiz')


