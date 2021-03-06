from rest_framework.test import APITestCase


class CountriesAPIV1Test(APITestCase):
    fixtures = ['countries', 'user']
    api_path = '/api/v1'
    api_host = 'testserver'

    def setUp(self):
        self.client.login(username='api-user@example.com', password='password')

    def test_countries(self):
        response = self.client.get(self.api_path + '/countries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 2)
