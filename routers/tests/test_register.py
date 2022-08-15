import pytest
from fastapi.testclient import TestClient
from main import app
from models.database_models import DBUser

client = TestClient(app)


@pytest.mark.parametrize('username,password,email,expected_status', [
    ('testuser', 'Heladera65', 'test@test.com', 200),
    ('shor', 'Heladera65', 'test@test.com', 422),
    ('testuser1', 'short', 'test@test.com', 422),
    ('testuser2', 'Heladera65', 'notamail', 422),
])
def test_register(username, password, email, expected_status):
    user_data = {'username': username, 'password': password, 'email': email}
    response = client.post('/users/register', json=user_data)
    assert response.status_code == expected_status or response.json()['status'] == expected_status
    if expected_status == 200:
        assert DBUser.get(DBUser.username == username)
    else:
        with pytest.raises(DBUser.DoesNotExist):
            DBUser.get(DBUser.username == username)


def test_register_user_already_taken():
    username = 'therealtestuser'
    user_data = {'username': username, 'password': 'Heladera65', 'email': 'realtestuser@test.com'}
    response1 = client.post('/users/register', json=user_data)
    response2 = client.post('/users/register', json=user_data)
    assert response1.status_code == 200 or response1.json()['status'] == 200
    assert response2.status_code == 400 or response2.json()['status'] == 400
    users = DBUser.select().where(DBUser.username == username)
    assert users.count() == 1
