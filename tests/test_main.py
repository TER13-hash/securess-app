import pytest
from app.main import app, is_valid_username


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# --- /health ---

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


# --- /greet ---

def test_greet_valid(client):
    response = client.post('/greet', json={"username": "jerald"})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, jerald!"}


def test_greet_missing_field(client):
    response = client.post('/greet', json={})
    assert response.status_code == 400


def test_greet_no_body(client):
    response = client.post('/greet', content_type='application/json', data='')
    assert response.status_code == 400


def test_greet_invalid_username_special_chars(client):
    response = client.post('/greet', json={"username": "drop; --"})
    assert response.status_code == 422


def test_greet_invalid_username_too_short(client):
    response = client.post('/greet', json={"username": "ab"})
    assert response.status_code == 422


def test_greet_invalid_username_too_long(client):
    response = client.post('/greet', json={"username": "a" * 21})
    assert response.status_code == 422


# --- Validator unit tests ---

def test_validator_accepts_valid():
    assert is_valid_username("jerald") is True


def test_validator_rejects_short():
    assert is_valid_username("ab") is False


def test_validator_rejects_special():
    assert is_valid_username("admin'--") is False
