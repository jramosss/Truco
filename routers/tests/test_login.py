import pytest
from fastapi.testclient import TestClient
from main import app
from models.database_models import DBUser
import bcrypt
from utils import is_expected_status
from re import match

client = TestClient(app)


@pytest.mark.parametrize('identifier, password, register', [
    ('testuser', 'Heladera65', True),
    ('testuser1', 'Heladera65', False),
    ('test@test.com', 'Heladera65', True),
    ('test1@test.com', 'Heladera65', False),
])
def test_login(identifier, password, register):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {'identifier': identifier, 'password': hashed_password}
    if register:
        email_regex = r"/^[a-zA-Z0-9.! #$%&'*+/=? ^_`{|}~-]+@[a-zA-Z0-9-]+(?:\. [a-zA-Z0-9-]+)*$/."
        if match(email_regex, identifier):
            DBUser.create(**{'username': 'testuser2', 'password': hashed_password, 'email': identifier})
        else:
            DBUser.create(**{'username': identifier, 'password': hashed_password, 'email': 'test@test.com'})
    user_data['password'] = password
    response = client.post('/users/login', json=user_data)
    expected_status = 200 if register else 404
    assert is_expected_status(response, expected_status)


@pytest.mark.parametrize('identifier, password, expected_status', [
    ('', 'Heladera65', 422),
    ('testuser', '', 422),
])
def test_login_missing_credentials(identifier, password, expected_status):
    user_data = {'identifier': identifier, 'password': password}
    response = client.post('/users/login', json=user_data)
    assert is_expected_status(response, expected_status)
