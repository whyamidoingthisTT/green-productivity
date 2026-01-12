from pydantic import BaseModel
from uuid import UUID
from datetime import date

class ReflectionCreate(BaseModel):
    date: date
    mood: int  # 1–5
    energy: str
    gratitude_note: str | None = None

class ReflectionResponse(BaseModel):
    id: UUID
    date: date
    mood: int
    energy: str
    gratitude_note: str | None

    class Config:
        from_attributes = True
