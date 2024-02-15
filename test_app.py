import pytest
from app import app, db

@pytest.fixture
def test_home_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Home Page" in response.data
    assert b'Login successful' in response.data
    assert current_user.is_authenticated

    # Clean up test user
    db.session.delete(test_user)
    db.session.commit()
