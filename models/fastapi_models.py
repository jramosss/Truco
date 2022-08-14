from pydantic import BaseModel, Field
from typing import Optional
from src.state import GameState, RoomState


class User(BaseModel):
    username: str = Field(max_length=20, min_length=5)
    password: str = Field(max_length=64, min_length=8, regex="^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$")
    email: str = Field(regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    validated: Optional[bool] = Field(default=False)


class Room(BaseModel):
    name: str = Field(max_length=20, min_length=5)
    max_players: int = Field(ge=2, le=6)
    owner: User
    status: str = Field(default=RoomState.LOBBY)
    users: list = Field(default=[])


class Game(BaseModel):
    room: Room
    state: str = Field(default=GameState.FIRST_HAND)
    turn: int = Field(default=0)
