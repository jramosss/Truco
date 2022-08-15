import pytest
from fastapi.testclient import TestClient
from main import app
from models.database_models import DBUser
import bcrypt

client = TestClient(app)


@pytest.mark.parametrize('username,password,email, register', [
    ('testuser', 'Heladera65', 'test@test.com', True),
    ('testuser1', 'Heladera65', 'test@test.com', False),
])
def test_login(username, password, email, register):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {'username': username, 'password': hashed_password, 'email': email}
    if register:
        DBUser.create(**user_data)
    user_data['password'] = password
    response = client.post('/users/login', json=user_data)
    status_code = response.json()['status']
    expected_status = 200 if register else 404
    assert status_code == expected_status
