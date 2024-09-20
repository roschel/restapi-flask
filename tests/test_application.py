import pytest
from application import create_app


class TestApplication:
    @pytest.fixture()
    def client(self):
        app = create_app('config.MockConfig')
        yield app.test_client()

    def test_get_users(self, client):
        # GIVEN
        # WHEN
        response = client.get('/users')

        # THEN
        assert response.status_code == 200
