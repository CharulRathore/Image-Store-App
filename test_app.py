import pytest
from app import app, db

@pytest.fixture
def test_home_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Home Page" in response.data
