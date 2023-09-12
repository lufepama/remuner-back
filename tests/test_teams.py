import pytest
import factory
from model_bakery import baker
from database.models import User, Team
from fastapi.testclient import TestClient
from main import app

class UserFactory(factory.Factory):
    class Meta:
        model = User
    id = 1
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')

class TeamFactory(factory.Factory):
    class Meta:
        model = Team
    id = 1
    name = factory.Faker('name')


class TestTeams():
    @pytest.fixture
    def test_data(self):
        return TestClient(app), UserFactory.build(), TeamFactory.build()
    
    def test_create_team(self, test_data):
        api_client, _, _ = test_data
        data = {"name": "Team_test"}
        response = api_client.post("/teams/", json=data)
        assert response.status_code == 201
    
    def test_get_teams(self, test_data):
        api_client, _, _ = test_data
        response = api_client.get("/teams/")
        assert response.status_code == 200

    
    def test_get_user_list_in_team(self, test_data):
        api_client, _, team = test_data
        response = api_client.get(f"/teams/{team.id}/user-list")
        assert response.status_code == 200