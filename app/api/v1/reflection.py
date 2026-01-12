from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.reflection import DailyReflection
from app.schemas.reflection import ReflectionCreate, ReflectionResponse
from app.core.deps import get_db

router = APIRouter()

@router.post("/", response_model=ReflectionResponse)
def create_reflection(data: ReflectionCreate, db: Session = Depends(get_db)):
    existing = db.query(DailyReflection).filter(
        DailyReflection.date == data.date
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Reflection already exists for this date")

    reflection = DailyReflection(**data.dict())
    db.add(reflection)
    db.commit()
    db.refresh(reflection)
    return reflection

@router.get("/", response_model=list[ReflectionResponse])
def list_reflections(db: Session = Depends(get_db)):
    return db.query(DailyReflection).all()
