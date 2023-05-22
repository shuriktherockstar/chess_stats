from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from schemas import player as player_schemas
from services.player_service import PlayerService

router = APIRouter(prefix='/players')


@router.post('/')
async def create_player(player: player_schemas.PlayerCreate,
                        session: Session = Depends(get_session)):
    player_service = PlayerService(session)
    return await player_service.create_player(player)


@router.get('/')
async def get_all_players(session: Session = Depends(get_session)):
    player_service = PlayerService(session)
    return await player_service.get_all_players()

@router.get('/{player_id}')
async def get_player(player_id: int,
                     session: Session = Depends(get_session)):
    player_service = PlayerService(session)
    return await player_service.get_player(player_id)


@router.delete('/{player_id}')
async def delete_player(player_id: int,
                        session: Session = Depends(get_session)):
    player_service = PlayerService(session)
    return await player_service.delete_player(player_id)
