from sqlalchemy.orm import Session
from sqlalchemy import func, case
from datetime import date, timedelta

from app.models.task import Task, TaskDifficulty
from app.models.focus_session import FocusSession
from app.models.reflection import DailyReflection

DIFFICULTY_WEIGHTS = {
    TaskDifficulty.easy: 1,
    TaskDifficulty.medium: 2,
    TaskDifficulty.hard: 3,
}
def daily_completion_percentage(db: Session, target_date: date):
    total = db.query(Task).filter(
        func.date(Task.created_at) == target_date,
        Task.is_deleted == False
    ).count()

    if total == 0:
        return 0.0

    completed = db.query(Task).filter(
        func.date(Task.created_at) == target_date,
        Task.is_completed == True,
        Task.is_deleted == False
    ).count()

    return round((completed / total) * 100, 2)
def weighted_productivity_score(db: Session, target_date: date):
    tasks = db.query(Task).filter(
        func.date(Task.created_at) == target_date,
        Task.is_deleted == False
    ).all()

    if not tasks:
        return 0.0

    total_weight = sum(DIFFICULTY_WEIGHTS[t.difficulty] for t in tasks)
    completed_weight = sum(
        DIFFICULTY_WEIGHTS[t.difficulty]
        for t in tasks if t.is_completed
    )

    return round((completed_weight / total_weight) * 100, 2)
def focus_minutes_for_day(db: Session, target_date: date):
    minutes = db.query(
        func.coalesce(func.sum(FocusSession.duration_minutes), 0)
    ).filter(
        func.date(FocusSession.start_time) == target_date
    ).scalar()

    return int(minutes)
def weekly_productivity_trend(db: Session):
    today = date.today()
    data = []

    for i in range(7):
        d = today - timedelta(days=i)
        score = weighted_productivity_score(db, d)
        data.append({
            "date": d,
            "productivity_score": score
        })

    return list(reversed(data))
def mood_productivity_pairs(db: Session):
    reflections = db.query(DailyReflection).all()
    result = []

    for r in reflections:
        score = weighted_productivity_score(db, r.date)
        result.append({
            "date": r.date,
            "mood": r.mood,
            "productivity_score": score
        })

    return result
