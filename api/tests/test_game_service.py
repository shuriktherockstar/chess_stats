import pytest
from sqlalchemy.orm import Session

from models.player import Player
from models.game import Game
from services.player_service import PlayerService
from services.game_service import GameService


@pytest.mark.asyncio
async def test_create_game(test_session: Session):
    player_service = PlayerService(test_session)
    game_service = GameService(test_session)

    test_player1 = Player(name='Magnus', surname='Carlsen')
    created_player1 = await player_service.create_player(test_player1)

    test_player2 = Player(name='Ding', surname='Liren')
    created_player2 = await player_service.create_player(test_player2)

    test_game = Game(player1_id=created_player1.id,
                     player2_id=created_player2.id,
                     result='First won')
    created_game = await game_service.create_game(test_game)

    game = test_session.query(Game).filter(Game.id == created_game.id).first()
    assert game is not None
    assert game.player1_id == created_player1.id
    assert game.player2_id == created_player2.id
    assert game.result == 'First won'


@pytest.mark.asyncio
async def test_get_all_games(test_session: Session):
    service = GameService(test_session)
    games = await service.get_all_games()

    assert games is not None


@pytest.mark.asyncio
async def test_get_game(test_session: Session):
    test_player1 = Player(name='Magnus', surname='Karlsen')
    test_player2 = Player(name='Ding', surname='Liren')

    test_session.add_all([test_player1, test_player2])
    test_session.commit()

    test_game = Game(player1_id=test_player1.id, player2_id=test_player2.id, result='Tie')
    test_session.add(test_game)
    test_session.commit()

    service = GameService(test_session)
    game = await service.get_game(test_game.id)

    assert game is not None
    assert game.player1_id == test_player1.id
    assert game.player2_id == test_player2.id
    assert game.result == 'Tie'


@pytest.mark.asyncio
async def test_delete_game(test_session: Session):
    test_player1 = Player(name='Magnus', surname='Karlsen')
    test_player2 = Player(name='Ding', surname='Liren')

    test_session.add_all([test_player1, test_player2])
    test_session.commit()

    test_game = Game(player1_id=test_player1.id, player2_id=test_player2.id, result='Tie')
    test_session.add(test_game)
    test_session.commit()

    service = GameService(test_session)
    await service.delete_game(test_game.id)

    game = test_session.query(Game).filter(Game.id == test_game.id).first()
    assert game is None
