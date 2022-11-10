from fastapi.testclient import TestClient
from .main import app, name

client = TestClient(app)

def test_token():
    response = client.get("/users/me")
    assert response.status_code == 200