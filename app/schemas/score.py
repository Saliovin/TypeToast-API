from pydantic import BaseModel
from datetime import datetime


class ScoreBase(BaseModel):
    name: str
    wpm: int
    accuracy: float
    correct: int
    incorrect: int
    extra: int
    missed: int


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int
    datetime: datetime

    class Config:
        orm_mode = True
