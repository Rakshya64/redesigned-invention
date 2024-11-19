import unittest
from app import app


class RouteTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_invalid_method_products_route(self):
        response = self.client.post('/products')  # Assuming /products only accepts GET
        self.assertEqual(response.status_code, 405)

    def test_invalid_method_home_route(self):
        # Test if the /home route returns a 405 when using POST instead of GET
        response = self.client.post('/')  # Attempt a POST request on a GET-only route
        self.assertEqual(response.status_code, 405)  # Expect 405 Method Not Allowed

if __name__ == '__main__':
    unittest.main()
