from pydantic import BaseModel, ConfigDict
import datetime
from uuid import UUID

class GameCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    studio: str
    slug: str
    ratings: int
    platforms: list[str]

class Game(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    _id: UUID
    name: str
    studio: str
    slug: str
    ratings: int
    platforms: list[str]
    release_date: datetime.datetime