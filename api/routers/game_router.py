from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import game as game_schemas
from services.game_service import GameService
from database import get_session

router = APIRouter(prefix='/games')


@router.post('/')
async def create_game(game: game_schemas.GameCreate,
                      session: Session = Depends(get_session)):
    game_service = GameService(session)
    return await game_service.create_game(game)


@router.get('/')
async def get_all_games(session: Session = Depends(get_session)):
    game_service = GameService(session)
    return await game_service.get_all_games()


@router.get('/{game_id}')
async def get_game(game_id: int,
                   session: Session = Depends(get_session)):
    game_service = GameService(session)
    return await game_service.get_game(game_id)


@router.delete('/{game_id}')
async def delete_game(game_id: int,
                      session: Session = Depends(get_session)):
    game_service = GameService(session)
    return await game_service.delete_game(game_id)
