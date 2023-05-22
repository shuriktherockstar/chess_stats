import re
from sqlalchemy.orm import Session

from models import player as player_models
from schemas import player as player_schemas


class PlayerService:
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def is_valid_player(player: player_schemas.PlayerCreate):
        if not player.name or not player.surname:
            return False
        permitted_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\'- '
        return set(player.name).issubset(permitted_chars) and set(player.surname).issubset(permitted_chars)

    @staticmethod
    def capitalize_player(player):
        player.name = re.sub(r"(^|\s|'|\-)(\S)",
                             lambda match: match.group(1) + match.group(2).upper(), player.name)
        player.surname = re.sub(r"(^|\s|'|\-)(\S)",
                                lambda match: match.group(1) + match.group(2).upper(), player.surname)
        return player

    async def create_player(self, player: player_schemas.PlayerCreate):
        db_player = player_models.Player(name=player.name, surname=player.surname)
        if self.is_valid_player(db_player):
            valid_player = self.capitalize_player(db_player)
            self.session.add(valid_player)
            self.session.commit()
            self.session.refresh(valid_player)
        return db_player

    async def get_all_players(self):
        db_players = self.session.query(player_models.Player).all()
        return [db_player for db_player in db_players]

    async def get_player(self, player_id: int):
        db_player = self.session.query(player_models.Player).filter(
            player_models.Player.id == player_id
        ).first()
        return db_player

    async def delete_player(self, player_id: int):
        db_player = await self.get_player(player_id)
        if db_player:
            self.session.delete(db_player)
            self.session.commit()
