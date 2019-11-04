from django.test import TestCase, Client
from .models import Card, User, Event, GameState

class overrallTestCase(TestCase):
    
    def test_client_makes_request(self):
        print("Initiating tests with user making requests to the API")
        tmp_client = Client()

        print("\nMaking request for create a new user on /get_user/")
        response = tmp_client.post('/cards/get_user/', {'username' : 'new_user'})
        self.assertEqual(response.status_code, 200)

        print("\nMaking request for retrieve user on /get_user/")
        response = tmp_client.post('/cards/get_user/', {'username' : 'new_user'})
        self.assertEqual(response.status_code, 200)

        print("\nRetrieving game state for user")
        response = tmp_client.post('/cards/get_game_state/', {'username' : 'new_user'})
        self.assertEqual(response.status_code, 200)

        print("\nRetrieving game state for user that doesn't exists")
        response = tmp_client.post('/cards/get_game_state/', {'username' : 'other_user'})
        self.assertEqual(response.status_code, 400)

        return