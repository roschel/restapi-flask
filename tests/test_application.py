from copy import deepcopy
from http.client import responses

import pytest
from pymongo.common import validate_list

from application import create_app


class TestApplication:
    @pytest.fixture()
    def client(self):
        app = create_app('config.MockConfig')
        yield app.test_client()

    @pytest.fixture()
    def valid_user(self):
        return {
            "first_name": "João",
            "last_name": "Roschel",
            "email": "joao@email.com",
            "cpf": "800.889.910-75",
            "birth_date": "1991-12-10"
        }

    @pytest.fixture()
    def invalid_user(self, valid_user):
        invalid_user = deepcopy(valid_user)
        invalid_user["cpf"] = "800.889.910-79"
        return invalid_user

    def test_get_users(self, client):
        # GIVEN
        # WHEN
        response = client.get('/users')

        # THEN
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post("/user", json=valid_user)
        assert response.status_code == 201
        assert b'sucessfully' in response.data

        response = client.post("/user", json=invalid_user)
        assert response.status_code == 400
        assert b'invalid' in response.data

    def test_get_user(self, client, valid_user):
        response = client.get(f"/user/{valid_user['cpf']}")
        assert response.status_code == 200
        assert response.json[0]["first_name"] == valid_user["first_name"]

    def test_get_user_does_not_exists(self, client, invalid_user):
        response = client.get(f"/user/{invalid_user['cpf']}")
        assert response.status_code == 404
        assert b'does not exist' in response.data
