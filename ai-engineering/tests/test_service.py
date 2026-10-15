import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from ai_path.service import make_server


class ServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(port=0, credentials={'demo-token':'demo', 'other-token':'other'})
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def post(self, data, token='demo-token'):
        request = Request(self.base + '/v1/search', data=json.dumps(data).encode(),
                          headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
        try:
            with urlopen(request, timeout=2) as response:
                return response.status, json.load(response)
        except HTTPError as response:
            with response:
                return response.code, json.load(response)

    def test_healthy(self):
        with urlopen(self.base + '/health', timeout=2) as response:
            self.assertEqual(json.load(response)['status'], 'ok')

    def test_authentication_and_invalid_shape(self):
        self.assertEqual(self.post({'query':'battery'}, token='wrong')[0], 401)
        self.assertEqual(self.post({'query':'battery'}, token='\u00e9')[0], 401)
        self.assertEqual(self.post({'query':'battery', 'tenant':'other'})[0], 400)
        self.assertEqual(self.post({'query':'battery', 'k':True})[0], 400)
        self.assertEqual(self.post([])[0], 400)

    def test_success_and_identity_derived_tenant(self):
        status, body = self.post({'query':'CAL-OTHER-99 calibration', 'k':10})
        self.assertEqual(status, 200)
        self.assertEqual(body['tenant'], 'demo')
        self.assertNotIn('other-private', [row['id'] for row in body['hits']])
        _, own = self.post({'query':'CAL-OTHER-99'}, token='other-token')
        self.assertIn('other-private', [row['id'] for row in own['hits']])

    def test_capacity_rejects_concurrent_request(self):
        entered, release = threading.Event(), threading.Event()

        class SlowIndex:
            def search(self, *args, **kwargs):
                entered.set()
                if not release.wait(timeout=3):
                    raise RuntimeError('test did not release request')
                return []

        server = make_server(port=0, credentials={'t':'demo'}, index=SlowIndex(), max_inflight=1)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        url = f'http://127.0.0.1:{server.server_port}/v1/search'

        def call():
            req = Request(url, data=b'{"query":"battery"}', headers={'Authorization':'Bearer t'})
            try:
                with urlopen(req, timeout=4) as response:
                    return response.status
            except HTTPError as response:
                with response:
                    return response.code

        first_result = []
        first = threading.Thread(target=lambda:first_result.append(call()), daemon=True)
        try:
            first.start()
            self.assertTrue(entered.wait(timeout=2))
            self.assertEqual(call(), 429)
        finally:
            release.set()
            first.join(timeout=4)
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.assertEqual(first_result, [200])


if __name__ == '__main__':
    unittest.main()
