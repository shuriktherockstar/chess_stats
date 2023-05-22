import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from models.player import Player
from models.game import Game


@pytest.mark.asyncio
async def test_create_game(test_session: Session, client: TestClient):
    test_player1 = Player(name='Magnus', surname='Carlsen')
    test_player2 = Player(name='Ding', surname='Liren')

    test_session.add_all([test_player1, test_player2])
    test_session.commit()

    test_game_data = {
        "player1_id": test_player1.id,
        "player2_id": test_player2.id,
        "result": "Tie"
    }

    response = client.post('/games/', json=test_game_data)
    created_game = test_session.query(Game).first()

    assert response.status_code == 200
    assert created_game.player1_id == test_game_data['player1_id']
    assert created_game.player2_id == test_game_data['player2_id']
    assert created_game.result == test_game_data['result']


@pytest.mark.asyncio
async def test_get_all_games(client: TestClient):
    response = client.get('/games/')
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_game(test_session: Session, client: TestClient):
    player1 = Player(name='Magnus', surname='Carlsen')
    player2 = Player(name='Ding', surname='Liren')
    test_session.add_all([player1, player2])
    test_session.commit()

    test_game = Game(player1_id=player1.id, player2_id=player2.id, result='Tie')
    test_session.add(test_game)
    test_session.commit()

    response = client.get(f'/games/{test_game.id}')
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['player1_id'] == test_game.player1_id
    assert response_data['player2_id'] == test_game.player2_id
    assert response_data['result'] == test_game.result


@pytest.mark.asyncio
async def test_delete_game(test_session: Session, client: TestClient):
    player1 = Player(name='Magnus', surname='Carlsen')
    player2 = Player(name='Ding', surname='Liren')
    test_session.add_all([player1, player2])
    test_session.commit()

    test_game = Game(player1_id=player1.id, player2_id=player2.id, result='Tie')
    test_session.add(test_game)
    test_session.commit()

    response = client.delete(f'/games/{test_game.id}')
    deleted_game = test_session.query(Game).filter(Game.id == test_game.id).first()

    assert response.status_code == 200
    assert deleted_game is None