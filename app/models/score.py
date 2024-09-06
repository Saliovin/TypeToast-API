from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Double,
    Integer,
    String,
)

from app.database import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    wpm = Column(Integer, index=True)
    accuracy = Column(Double)
    correct = Column(Integer)
    incorrect = Column(Integer)
    extra = Column(Integer)
    missed = Column(Integer)
    datetime = Column(DateTime, default=datetime.now(), index=True)
