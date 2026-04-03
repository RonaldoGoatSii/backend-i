import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_meeting_data():
    return {
        "title": "Planning Mensal",
        "date": "2026-03-10",
        "owner": "Jorge",
        "participants": ["Ana"]
    }