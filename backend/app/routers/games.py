from fastapi import APIRouter
from sqlalchemy.orm import Session
from database.db import get_db
from games import schemas, crud
from fastapi import Depends, HTTPException

router = APIRouter()

@router.post("/games/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_game = crud.get_game_by_name(db, name=game.name)
    if db_game:
        raise HTTPException(status_code=400, detail="Name already registered")
    if len(game.name) < 10:
        raise HTTPException(status_code=422, detail="Name length need < 10")
    return crud.create_game(db=db, game=game)


@router.get("/games/", response_model=list[schemas.Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games


@router.get("/games/{game_id}", response_model=schemas.Game)
def read_game(game_id: int, db: Session = Depends(get_db)):
    db_game = crud.get_game(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game