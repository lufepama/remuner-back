import pytest
from fastapi.testclient import TestClient
from main import app


class TestIntegrations:
    @pytest.fixture
    def api_client(self):
        return TestClient(app)
 
    def test_create_integrations(self, api_client):
        user_data = {
            "name": "Integration 1",
            "type": "Type 1",
            "status": True
        }
        response = api_client.post("/integrations/", json=user_data)
        assert response.status_code == 201
    
    def test_get_integrations(self, api_client):
        response = api_client.get("/integrations/")
        assert response.status_code == 200