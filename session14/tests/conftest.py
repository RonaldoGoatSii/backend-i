import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Cria um cliente de teste para a API"""
    return TestClient(app)

@pytest.fixture
def valid_meeting_data():
    """Fornece dados válidos para criar uma reunião"""
    return {
        "title": "Sprint Planning",
        "date": "2026-05-10",
        "owner": "Jorge",
        "participants": ["Ana", "Pedro"]
    }