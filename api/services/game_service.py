from sqlalchemy.orm import Session
from sqlalchemy import desc

from models import game as game_models
from schemas import game as game_schemas


class GameService:
    def __init__(self, session: Session):
        self.session = session

    async def create_game(self, game: game_schemas.GameCreate):
        db_game = game_models.Game(player1_id=game.player1_id, player2_id=game.player2_id, result=game.result)
        self.session.add(db_game)
        self.session.commit()
        self.session.refresh(db_game)
        return db_game

    async def get_all_games(self):
        db_games = self.session.query(game_models.Game).order_by(game_models.Game.id.desc()).all()
        return db_games

    async def get_game(self, game_id: int):
        db_game = self.session.query(game_models.Game).filter(game_models.Game.id == game_id).first()
        return db_game

    async def delete_game(self, game_id: int):
        db_game = await self.get_game(game_id)
        game_id = db_game.id
        if db_game:
            self.session.delete(db_game)
            self.session.commit()
        return {
            'message': f'Матч с id = {game_id} успешно удален'
        }
