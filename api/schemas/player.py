from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    surname: str


class PlayerCreate(PlayerBase):
    pass


class PlayerDelete(PlayerBase):
    id: int


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True
