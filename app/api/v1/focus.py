from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.focus_session import FocusSession
from app.schemas.focus_session import (
    FocusSessionCreate,
    FocusSessionEnd,
    FocusSessionResponse
)
from app.core.deps import get_db

router = APIRouter()

@router.post("/", response_model=FocusSessionResponse)
def start_focus_session(data: FocusSessionCreate, db: Session = Depends(get_db)):
    session = FocusSession(
        task_id=data.task_id,
        start_time=data.start_time
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

@router.patch("/{session_id}/end", response_model=FocusSessionResponse)
def end_focus_session(session_id: str, data: FocusSessionEnd, db: Session = Depends(get_db)):
    session = db.query(FocusSession).filter(FocusSession.id == session_id).first()
    session.end_time = data.end_time
    delta = session.end_time - session.start_time
    session.duration_minutes = int(delta.total_seconds() // 60)
    db.commit()
    db.refresh(session)
    return session
