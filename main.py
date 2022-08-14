from fastapi import FastAPI
from routers.users import router as users_router
from models.database_models import db, DBGame, DBRoom, DBUser


app = FastAPI()
db.connect()
db.create_tables([DBUser, DBRoom, DBGame])
app.include_router(users_router)
