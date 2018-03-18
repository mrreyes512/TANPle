import pytest
import os
import json
from app import app
import heroku_db_creds

# os.environ['DATABASE_URL'] = 'FIX_ME_TO_LOOK_AT ../database_creds.py'
os.environ['DATABASE_URL'] = 'postgres://ylbzmiqhvzznyp:1a0c5aa46adada3c12335e44ff26cc3dba1d0d8cf70c5938dd910a205874f6c9@ec2-50-19-105-188.compute-1.amazonaws.com:5432/dddev09qk12ksl'


@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    app_client = app.test_client()

    return app_client


@pytest.fixture
def sampleJsonInput():
    with open('test/requests/query_line.json', 'r') as f:
        json_data = f.read()
    input = json.loads(json_data)
    # input = str(var)
    # with open('requests/query_line.json') as json_data:
    #     input = json.load(json_data)

    return json_data


def test_webhookresponse(client, sampleJsonInput):
    resp = client.post('/webhook', data=sampleJsonInput)
    assert resp.status_code == 200

