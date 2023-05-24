from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)

    player1 = relationship('Game', cascade='all,delete', backref='player1', foreign_keys='Game.player1_id')
    player2 = relationship('Game', cascade='all,delete', backref='player2', foreign_keys='Game.player2_id')
