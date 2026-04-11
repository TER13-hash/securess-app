import json
from app.main import app

def test_add_success():
    client = app.test_client()
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_add_invalid_input():
    client = app.test_client()
    response = client.post("/add", json={"a": "x", "b": 3})
    assert response.status_code == 400
