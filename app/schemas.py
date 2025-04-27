from pydantic import BaseModel
from typing import List


class Quiz(BaseModel):
    id: int
    question: str
    choice1: str
    choice2: str
    choice3: str
    choice4: str
    correct_choice: int

    class Config:
        orm_mode = True


class QuizListResponse(BaseModel):
    quizzes: List[Quiz]
