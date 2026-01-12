import uuid
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.models.base import TimestampMixin

class DailyReflection(Base, TimestampMixin):
    __tablename__ = "daily_reflections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    date = Column(Date, nullable=False, unique=True)
    mood = Column(Integer, nullable=False)  # 1–5
    energy = Column(String, nullable=False) # low / medium / high
    gratitude_note = Column(String, nullable=True)
