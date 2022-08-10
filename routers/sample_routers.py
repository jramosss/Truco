from fastapi import APIRouter
from db.models import User, Room, Game


router = APIRouter()


@router.get("/")
async def read_root():
    # user = User.create(username="test", password="test")
    # print(user.username)
    user = User.get(User.username == "test")
    print(user.__dict__)
