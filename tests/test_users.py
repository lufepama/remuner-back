import pytest
from fastapi.testclient import TestClient
from main import app


class TestUsers:
    @pytest.fixture
    def api_client(self):
        return TestClient(app)
 
    def test_create_user(self, api_client):
        """
            Verifies the user creation
        """
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "status": True
        }
        response = api_client.post("/users/", json=user_data)
        assert response.status_code == 201
    
    def test_get_users(self, api_client):
        """
            Verifies the users saved in db
        """
        response = api_client.get("/users/")
        assert response.status_code == 200