from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.orm import Mapped, declarative_base

Base = declarative_base()


class Record(Base):
    __tablename__ = "company"
    id: Mapped[int] = Column(Integer, primary_key=True)
    created_at: Mapped[datetime] = Column(TIMESTAMP(timezone=True))
    name: Mapped[str] = Column(String)
    wpm: Mapped[int] = Column(Integer)
    accuracy: Mapped[int] = Column(Integer)
    correct: Mapped[int] = Column(Integer)
    incorrect: Mapped[int] = Column(Integer)
    extra: Mapped[int] = Column(Integer)
    missed: Mapped[int] = Column(Integer)
