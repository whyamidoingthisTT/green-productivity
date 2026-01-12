from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.core.deps import get_db
from app.services.analytics import (
    daily_completion_percentage,
    weighted_productivity_score,
    focus_minutes_for_day,
    weekly_productivity_trend,
    mood_productivity_pairs
)

router = APIRouter()

@router.get("/daily-summary")
def daily_summary(target_date: date, db: Session = Depends(get_db)):
    return {
        "date": target_date,
        "completion_percentage": daily_completion_percentage(db, target_date),
        "productivity_score": weighted_productivity_score(db, target_date),
        "focus_minutes": focus_minutes_for_day(db, target_date)
    }

@router.get("/weekly-trend")
def weekly_trend(db: Session = Depends(get_db)):
    return weekly_productivity_trend(db)

@router.get("/mood-correlation")
def mood_correlation(db: Session = Depends(get_db)):
    return mood_productivity_pairs(db)
