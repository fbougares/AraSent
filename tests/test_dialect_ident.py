from fastapi.testclient import TestClient
from sources.datamodel.dialects import Dialects
from main import app


client = TestClient(app)

print(client)

def test_dialects_list():
    response = client.get("/dialects")
    assert response.status_code == 200
    assert response.json() == [d.value for d in Dialects]