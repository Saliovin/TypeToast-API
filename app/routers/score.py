import app.schemas.score as schemas
import app.crud.score as crud
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.create_score(db=db, score=score)


@router.get("/", response_model=list[schemas.Score])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    scores = crud.get_scores(db, skip=skip, limit=limit)
    return scores


@router.get("/weekly/", response_model=list[schemas.Score])
def read_weekly_leaderboard(db: Session = Depends(get_db)):
    scores = crud.get_weekly_leaderboard(db)
    return scores
