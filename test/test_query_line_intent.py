import pytest
import os
from app import app
import heroku_db_creds

# os.environ['DATABASE_URL'] = 'FIX_ME_TO_LOOK_AT ../database_creds.py'


@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()

    return client


@pytest.fixture
def sampleJsonInput():
    input = '''
                {
                  "id": "30aab522-1b70-4d9f-af7b-bc34090a4c3a",
                  "timestamp": "2018-02-19T19:50:32.268Z",
                  "lang": "en",
                  "result": {
                    "source": "agent",
                    "resolvedQuery": "line",
                    "action": "queryLine",
                    "actionIncomplete": false,
                    "parameters": {},
                    "contexts": [],
                    "metadata": {
                      "intentId": "644e2344-1458-49a3-ac6b-60c529cf58d2",
                      "webhookUsed": "true",
                      "webhookForSlotFillingUsed": "false",
                      "webhookResponseTime": 104,
                      "intentName": "2-queryLine"
                    },
                    "fulfillment": {
                      "speech": "Let me check that out for you(default response)",
                      "messages": [
                        {
                          "type": 0,
                          "speech": "Let me check that out for you(default response)"
                        }
                      ]
                    },
                    "score": 1
                  },
                  "status": {
                    "code": 206,
                    "errorType": "partial_content",
                    "errorDetails": "Webhook call failed. Error: 500 INTERNAL SERVER ERROR",
                    "webhookTimedOut": false
                  },
                  "sessionId": "08740915-d347-4698-8edb-6947f56fbea7"
                }
            '''
    return input


def test_webhookresponse(client, sampleJsonInput):
    resp = client.post('/webhook', data=sampleJsonInput)
    assert resp.status_code == 200

