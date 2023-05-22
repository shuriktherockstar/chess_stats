import pytest
from sqlalchemy.orm import Session

from models.player import Player
from schemas.player import PlayerCreate
from services.player_service import PlayerService


@pytest.mark.asyncio
async def test_is_valid_player():
    player = PlayerCreate(name='Magnus', surname='Carlsen')
    assert PlayerService.is_valid_player(player) is True

    player = PlayerCreate(name='', surname='Carlsen')
    assert PlayerService.is_valid_player(player) is False

    player = PlayerCreate(name='Magnus1', surname='Carlsen')
    assert PlayerService.is_valid_player(player) is False

    player = PlayerCreate(name="M'agnus", surname='Carlsen')
    assert PlayerService.is_valid_player(player) is True

    player = PlayerCreate(name='Magnus', surname='C arlsen')
    assert PlayerService.is_valid_player(player) is True


@pytest.mark.asyncio
async def test_capitalize_player():
    player = PlayerCreate(name='magnus', surname='carlsen')
    PlayerService.capitalize_player(player)
    assert player.name == 'Magnus' and player.surname == 'Carlsen'

    player = PlayerCreate(name='m agnus', surname='c arlsen')
    PlayerService.capitalize_player(player)
    assert player.name == 'M Agnus' and player.surname == 'C Arlsen'

    player = PlayerCreate(name="m'agnus", surname="c'arlsen")
    PlayerService.capitalize_player(player)
    assert player.name == "M'Agnus" and player.surname == "C'Arlsen"

    player = PlayerCreate(name="m-agnus", surname="c-arlsen")
    PlayerService.capitalize_player(player)
    assert player.name == "M-Agnus" and player.surname == "C-Arlsen"


@pytest.mark.asyncio
async def test_create_player(test_session: Session):
    test_player = Player(name='Magnus', surname='Carlsen')
    service = PlayerService(test_session)
    created_player = await service.create_player(test_player)

    player = test_session.query(Player).filter(Player.id == created_player.id).first()
    assert player is not None
    assert player.name == 'Magnus'
    assert player.surname == 'Carlsen'


@pytest.mark.asyncio
async def test_get_all_players(test_session: Session):
    service = PlayerService(test_session)
    players = await service.get_all_players()

    assert players is not None


@pytest.mark.asyncio
async def test_get_player(test_session: Session):
    test_player = Player(name='Magnus', surname='Carlsen')
    test_session.add(test_player)
    test_session.commit()

    service = PlayerService(test_session)
    player = await service.get_player(test_player.id)

    assert player is not None
    assert player.name == 'Magnus'
    assert player.surname == 'Carlsen'


@pytest.mark.asyncio
async def test_delete_player(test_session: Session):
    test_player = Player(name='Magnus', surname='Carlsen')
    test_session.add(test_player)
    test_session.commit()

    service = PlayerService(test_session)
    await service.delete_player(test_player.id)

    player = test_session.query(Player).filter(Player.id == test_player.id).first()
    assert player is None
