from fastapi import FastAPI
from routers.sample_routers import router as sample_router
from db.models import db, Game, Room, User


app = FastAPI()
db.connect()
db.create_tables([User, Room, Game])
app.include_router(sample_router)
