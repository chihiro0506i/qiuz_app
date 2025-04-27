from sqlalchemy import Column, Integer, String
from .database import Base


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    choice1 = Column(String, nullable=False)
    choice2 = Column(String, nullable=False)
    choice3 = Column(String, nullable=False)
    choice4 = Column(String, nullable=False)
    correct_choice = Column(Integer, nullable=False)
