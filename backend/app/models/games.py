import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from database.db import Base
import uuid

class Game(Base):
    __tablename__ = "game"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    studio: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(50), nullable=False)
    ratings: Mapped[int] = mapped_column(Integer(), nullable=False, default=20)
    platforms: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    release_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.utcnow)