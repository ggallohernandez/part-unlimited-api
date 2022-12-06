from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from parts.models import Part

# test loading a fixture that the route topword-list returns a list of top words
class TopWordsTestCase(TestCase):
    # mock topwords in the setup method
    def setUp(self):
        #create a test user and get a Bearer token
        self.user = User.objects.create_user(username='test', password='test')
                                             
        response = self.client.post(reverse('authenticate'), {'username': 'test', 'password': 'test'})
        
        self.bearerToken = response.json()['token']
        
        Part.objects.create(description='foo bar', weight_ounces=1, is_active=True)
        Part.objects.create(description='foo bar', weight_ounces=1, is_active=True)
        Part.objects.create(description='foo zaz', weight_ounces=1, is_active=True)

    def test_topwords(self):
        response = self.client.get(reverse('topword-list'), **{'HTTP_AUTHORIZATION': f'Bearer {self.bearerToken}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['word'], 'foo')
        self.assertEqual(response.json()[1]['word'], 'bar')
        self.assertEqual(response.json()[2]['word'], 'zaz')
        
        