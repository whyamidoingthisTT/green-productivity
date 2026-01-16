import uuid
import enum
from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.base import TimestampMixin

class TaskDifficulty(enum.Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class TaskCategory(enum.Enum):
    work = "work"
    study = "study"
    personal = "personal"

class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    difficulty = Column(Enum(TaskDifficulty), nullable=False)
    category = Column(Enum(TaskCategory), nullable=False)
    is_completed = Column(Boolean, default=False)

    focus_sessions= relationship(
    "FocusSession",
    back_populates="task",
    cascade="all, delete-orphan"
)

