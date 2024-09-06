from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.models.score import Score
from app.schemas.score import ScoreCreate


def get_scores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Score).offset(skip).limit(limit).all()


def get_weekly_leaderboard(db: Session):
    dt = datetime.now().date()
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=6)
    return (
        db.query(Score)
        .filter(Score.datetime >= start)
        .filter(Score.datetime <= end)
        .limit(20)
        .all()
    )


def create_score(db: Session, score: ScoreCreate):
    db_score = Score(**score.model_dump())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score
