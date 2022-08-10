from __future__ import annotations

from datetime import datetime, timezone

import peewee as models
from src.state import GameState as gs
from src.state import RoomState as rs
from typing_extensions import Self

db = models.SqliteDatabase("db.sqlite3")


GAME_STATES = (
    (gs.FIRST_HAND, "First Hand"),
    (gs.SECOND_HAND, "Second Hand"),
    (gs.THIRD_HAND, "Third Hand"),
    (gs.ENVIDO, "Envido"),
    (gs.TRUCO, "Truco"),
)

ROOM_STATES = (
    (rs.LOBBY, "Lobby"),
    (rs.INGAME, "In Game"),
    (rs.FINISHED, "Finished"),
)

class BaseModel(models.Model):
    created_at: datetime = models.DateTimeField(default=datetime.now(tz=timezone.utc))

    def get(self, *query, **filters) -> Self:
        return models.Model().get(*query, **filters)
    class Meta:
        database = db

class User(BaseModel):
    username: str = models.CharField(max_length=20)
    password: str = models.CharField(max_length=20)
    class Meta:
        database = db

class Room(BaseModel):
    name: str = models.CharField(max_length=20)
    max_players: int = models.IntegerField()
    owner: User = models.ForeignKeyField(User, backref='rooms')
    status: str = models.CharField(max_length=20, choices=ROOM_STATES, default=rs.LOBBY)
    users = models.ManyToManyField(User, backref='rooms')
    class Meta:
        database = db


class Game(BaseModel):
    room: Room = models.ForeignKeyField(Room, backref='games')
    state: str = models.CharField(max_length=20, choices=GAME_STATES)
    turn: int = models.IntegerField(default=0)
    class Meta:
        database = db
