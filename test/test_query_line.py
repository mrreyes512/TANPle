import pytest
from intents import query_line

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()



def test_query_line_get_data(client, sampleJsonInput):
    resp = client.post('/webhook', data=sampleJsonInput)
    assert resp.status_code == 200

