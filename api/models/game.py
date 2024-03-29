from sqlalchemy import Column, Integer, String, ForeignKey

from . import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    player1_id = Column(Integer, ForeignKey('players.id', ondelete='CASCADE'))
    player2_id = Column(Integer, ForeignKey('players.id', ondelete='CASCADE'))
    result = Column(String)

