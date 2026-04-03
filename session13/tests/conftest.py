import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_meeting_data():
    return {
        "title": "Sprint Planning",
        "date": "2026-05-10",
        "owner": "Jorge",
        "participants": ["Ana", "Pedro"]
    }

@pytest.fixture
def valid_action_item_data():
    return {
        "description": "Finalizar documentação",
        "owner": "Ana",
        "due_date": "2026-05-15"
    }