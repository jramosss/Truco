from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20)
    password = fields.CharField(max_length=20)
    created_at = fields.DatetimeField(auto_now_add=True)


class Room(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    max_players = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    owner = fields.ForeignKeyField('models.User', related_name='rooms')
    status = fields.CharField(max_length=20)
    users = fields.ManyToManyField('models.User', related_name='rooms')


class Game(Model):
    id = fields.IntField(pk=True)
    room = fields.ForeignKeyField('models.Room', related_name='games')
    state = fields.CharField(max_length=20)
    turn = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
