import pytest
from app import app, db, bcrypt

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.drop_all()

@pytest.fixture
def logged_in_client(client):
    # Assuming a logged-in user for testing protected routes
    with client:
        client.post('/login', data=dict(
            username='testuser',
            password='password'
        ))
        yield client

def test_register(client):
    response = client.post('/register', data=dict(
        username='testuser',
        password='password'
    ), follow_redirects=True)
    assert b"Login" in response.data

def test_login(client):
    response = client.post('/login', data=dict(
        username='testuser',
        password='password'
    ), follow_redirects=True)
    assert b"Dashboard" in response.data

def test_logout(logged_in_client):
    response = logged_in_client.get('/logout', follow_redirects=True)
    assert b"Login" in response.data


def test_upload_file(logged_in_client):
    data = {'file': (BytesIO(b'my file contents'), 'test.txt')}
    response = logged_in_client.post('/dashboard', data=data, content_type='multipart/form-data')
    assert b"File Uploaded" in response.data