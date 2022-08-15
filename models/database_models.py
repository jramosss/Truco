from datetime import datetime, timezone

import peewee as models
from src.state import GameState as gs
from src.state import RoomState as rs
from sys import argv

if 'test' in argv[0]:
    db = models.SqliteDatabase("testing_db.sqlite3")
else:
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

class DBUser(models.Model):
    username: str = models.CharField(max_length=20)
    password: str = models.CharField(max_length=20)
    email: str = models.CharField(max_length=20)
    validated: bool = models.BooleanField(default=False)
    created_at: datetime = models.DateTimeField(default=datetime.now(tz=timezone.utc))

    class Meta:
        database = db

class DBRoom(models.Model):
    name: str = models.CharField(max_length=20)
    max_players: int = models.IntegerField()
    owner: DBUser = models.ForeignKeyField(DBUser, backref='rooms')
    status: str = models.CharField(max_length=20, choices=ROOM_STATES, default=rs.LOBBY)
    users = models.ManyToManyField(DBUser, backref='rooms')
    created_at: datetime = models.DateTimeField(default=datetime.now(tz=timezone.utc))

    class Meta:
        database = db


class DBGame(models.Model):
    room: DBRoom = models.ForeignKeyField(DBRoom, backref='games')
    state: str = models.CharField(max_length=20, choices=GAME_STATES)
    turn: int = models.IntegerField(default=0)
    created_at: datetime = models.DateTimeField(default=datetime.now(tz=timezone.utc))

    class Meta:
        database = db
