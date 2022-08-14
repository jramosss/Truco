import bcrypt
from fastapi import APIRouter
from models.database_models import DBUser, db
from models.fastapi_models import User
from models.request_models import LoginRequest

router = APIRouter()


@router.post('/register')
def register(user: User):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user = DBUser.create(username=user.username, password=hashed_password, email=user.email)
    return user


@router.post('/login')
def login(request: LoginRequest):
    if not (request.email or request.username):
        return {'error': 'Username or email is required', 'status': 400}
    elif request.username:
        user = DBUser.get(DBUser.username == request.username)
    elif request.email:
        user = DBUser.get(DBUser.email == request.email)
    if not user:
        return {'error': 'User not found', 'status': 404}
    if bcrypt.checkpw(request.password.encode('utf-8'), user.password.encode('utf-8')):
        return {'user': user, 'status': 200}
    else:
        return {'error': 'Wrong password', 'status': 401}


@router.get('/users')
def get_users():
    users = DBUser.select()
    return {'users': list(users.execute(db))}
