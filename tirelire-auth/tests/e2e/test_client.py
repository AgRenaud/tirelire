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

    def test_add_user_and_authenticate(self):
        response = self.client.post(
            '/api/v1/create_user', 
            json=dict(
                id='123',
                password='my_password',
                first_name='john',
                last_name='doe',
                email='jdoe@mail.com'
            ))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            '/api/v1/authenticate', 
            json=dict(
                email='jdoe@mail.com',
                password='my_password',
            ))
        self.assertEqual(response.status_code, 200)

    def test_add_already_existing_email(self):
        response = self.client.post(
            '/api/v1/create_user', 
            json=dict(
                id='123abc',
                password='my_password',
                first_name='mat',
                last_name='someone',
                email='msome1@mail.com'
            ))
        
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            '/api/v1/create_user', 
            json=dict(
                id='abc123',
                password='my_password',
                first_name='marvin',
                last_name='someone',
                email='msome1@mail.com'
            ))
        
        self.assertEqual(response.status_code, 400)