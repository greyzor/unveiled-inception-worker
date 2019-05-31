"""
"""
from app import create_app
import pytest

IMG_FILE = 'tests/espresso.jpg'

@pytest.fixture
def client():
    """ """
    app = create_app()
    app.config['TESTING'] = True
    yield app.test_client()

def test_get_status(client):
    """ """
    res = client.get('/api/1/status').json
    assert(res['status'] == 'ok')

def test_post_image(client):
    """ """
    global IMG_FILE
    img = open(IMG_FILE, 'rb').read()

    res = client.post('/api/1/classify', data=img).json
    assert(res['status'] == 'done')
    assert(res['results'][0][1] == 'espresso')