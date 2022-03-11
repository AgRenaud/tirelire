from unittest import TestCase
from fastapi.testclient import TestClient
from testing.postgresql import Postgresql
from testing.redis import RedisServer

from app.entrypoints.api.client import create_app


class TestAPI(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pg = Postgresql(
            host='127.0.0.1',
            port=54321
        )
        cls.redis = RedisServer(
            redis_conf={'port': 65432, 'requirepass': 'MyRedisPassword'}
        )
        cls.client: TestClient = TestClient(create_app())

    @classmethod
    def tearDownClass(cls):
        cls.pg.stop()
        cls.redis.stop()

    def test_api_client(self):
        response = self.client.get('/docs')
        self.assertEqual(response.status_code, 200)
