from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class FocusSessionCreate(BaseModel):
    task_id: UUID | None = None
    start_time: datetime

class FocusSessionEnd(BaseModel):
    end_time: datetime

class FocusSessionResponse(BaseModel):
    id: UUID
    task_id: UUID | None
    start_time: datetime
    end_time: datetime | None
    duration_minutes: int

    class Config:
        from_attributes = True
