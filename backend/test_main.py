from fastapi.testclient import TestClient

from main import app

client = TestClient(app=app)


def test_server():
    response = client.get("/")
    assert response.status_code == 200
