import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from models.player import Player


@pytest.mark.asyncio
async def test_create_player(test_session: Session, client: TestClient):
    player_data = {
        'name': 'Magnus',
        'surname': 'Carlsen'
    }

    response = client.post('/players/', json=player_data)
    created_player = test_session.query(Player).first()

    assert response.status_code == 200
    assert created_player.name == player_data['name']
    assert created_player.surname == player_data['surname']


@pytest.mark.asyncio
async def test_get_all_players(client: TestClient):
    response = client.get('/players/')
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_player(test_session: Session, client: TestClient):
    test_player = Player(name='Magnus', surname='Carlsen')
    test_session.add(test_player)
    test_session.commit()

    response = client.get(f'/players/{test_player.id}')
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['name'] == 'Magnus'
    assert response_data['surname'] == 'Carlsen'


@pytest.mark.asyncio
async def test_delete_player(test_session, client: TestClient):
    test_player = Player(name='Magnus', surname='Carlsen')
    test_session.add(test_player)
    test_session.commit()

    response = client.delete(f'/players/{test_player.id}')
    deleted_player = test_session.query(Player).filter(Player.id == test_player.id).first()

    assert response.status_code == 200
    assert deleted_player is None
