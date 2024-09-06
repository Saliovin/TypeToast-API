from pydantic import BaseModel


class ScoreBase(BaseModel):
    name: str
    wpm: str
    accuracy: str
    correct: str
    incorrect: str
    extra: str
    missed: str


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int
    datetime: int

    class Config:
        orm_mode = True
