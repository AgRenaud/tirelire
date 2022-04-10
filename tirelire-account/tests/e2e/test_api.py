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

    def test_requests_return_200(self):
        add_holder = self.client.post('/v1/holders/')
        self.assertEqual(add_holder.status_code, 200)
        holder_id = add_holder.json().get('holder_id')
        query_holder = self.client.get(f'/v1/holders/{holder_id}')
        self.assertEqual(query_holder.status_code, 200)
        body = {
            "currency": "EUR"
        }
        add_account_to_holder = self.client.post(f'/v1/holders/{holder_id}/accounts', json=body)
        self.assertEqual(add_account_to_holder.status_code, 200)
        account_id = add_account_to_holder.json().get('account_id')
        body = {
            "operations": [
                {
                "name": "op1",
                "date": "2022-02-09",
                "value": -14.99,
                "currency": "EUR",
                "category": "FOOD"
                },
                {
                "name": "op2",
                "date": "2022-02-08",
                "value": -149.98,
                "currency": "EUR",
                "category": "BOOK"
                },
                {
                "name": "op3",
                "date": "2022-02-07",
                "value": 1260.65,
                "currency": "EUR",
                "category": "SALARY"
                },
            ]
        }
        add_operations_to_account = self.client.post(f'/v1/holders/{holder_id}/accounts/{account_id}/operations', json=body)
        self.assertEqual(add_operations_to_account.status_code, 200)
