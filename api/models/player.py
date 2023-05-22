from sqlalchemy import Column, Integer, String

from . import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
