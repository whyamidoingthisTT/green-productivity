from pydantic import BaseModel
from uuid import UUID
from enum import Enum

class TaskDifficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class TaskCategory(str, Enum):
    work = "work"
    study = "study"
    personal = "personal"

class TaskCreate(BaseModel):
    title: str
    difficulty: TaskDifficulty
    category: TaskCategory

class TaskUpdate(BaseModel):
    title: str | None = None
    difficulty: TaskDifficulty | None = None
    category: TaskCategory | None = None
    is_completed: bool | None = None

class TaskResponse(BaseModel):
    id: UUID
    title: str
    difficulty: TaskDifficulty
    category: TaskCategory
    is_completed: bool

    class Config:
        from_attributes = True
