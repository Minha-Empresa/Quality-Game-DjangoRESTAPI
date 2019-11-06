from django.test import TestCase, Client
from .models import Card, User, Event, GameState

class overrallTestCase(TestCase):

    def setUp(self):
        # card 1
        card_1 = Card()

        # card 2
        card_2 = Card()

        # card 3
        card_3 = Card()

        # card 4
        card_4 = Card()

        # card 5
        card_5 = Card()

        # user 1
        user_1 = User()

        # event 1
        event_1 = Event()

        # game state 1
        game_state_1 = GameState()
        pass

    def test_units(self):
        pass

    def test_client_requests_handling(self):

        # Firsts tests for client requests
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

        # Requesting Game State update
        print("\nMaking request for update game state for a existing user")
        response = tmp_client.post('/cards/save_game_state/', {'username': 'new_user',
            'game_cash' : '2399.00',
            'game_approval' : '96',
            'game_cli_satis' : '92',
            'game_emp_satis' : '93',
            'game_over_satis' : '90',
            'game_level': '1'})
        self.assertEqual(response.status_code, 200)

        print("\nMaking request for update game state for a NON existing user")
        response = tmp_client.post('/cards/save_game_state/', {'username': 'other_user',
            'game_cash' : '2399.00',
            'game_approval' : '96',
            'game_cli_satis' : '92',
            'game_emp_satis' : '93',
            'game_over_satis' : '90',
            'game_level': '1'})
        self.assertEqual(response.status_code,400)

        return