from sqlalchemy.orm import Session

from . import schemas
from models import games

def get_game(db: Session, game_id: int):
    return db.query(games.Game).filter(games.Game.id == game_id).first()


def get_game_by_name(db: Session, name: str):
    return db.query(games.Game).filter(games.Game.name == name).first()


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(games.Game).offset(skip).limit(limit).all()


def create_game(db: Session, game: schemas.GameCreate):
    db_game = games.Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game