from django.test import TestCase, Client
from .models import Card, User, Event, GameState
from .views import retrieve_event_list, create_new_game_state, create_new_user, get_game_state

class overrallTestCase(TestCase):

    def setUp(self):
        # card 1
        card_1 = Card()
        card_1.card_title = "Card de Planejamento"
        card_1.card_description = "Você está planej ..."
        card_1.card_level = 1
        card_1.card_ct_choice = "correct option"
        card_1.card_wr_choice = "wrong option"
        card_1.card_image_path = ""
        card_1.save()

        # event 1
        event_1 = Event()
        event_1.card = card_1
        event_1.card_cash_ct_effect = 20
        event_1.card_cash_wr_effect = -20
        event_1.card_approval_ct_effect = 2
        event_1.card_approval_wr_effect = -5
        event_1.save()

        # card 2
        card_2 = Card()
        card_2.card_title = "Card de Planejamento"
        card_2.card_description = "O escopo do projet ..."
        card_2.card_level = 1
        card_2.card_ct_choice = "correct option"
        card_2.card_wr_choice = "wrong option"
        card_2.card_image_path = ""
        card_2.save()

        # event 2
        event_2 = Event()
        event_2.card = card_2
        event_2.card_cash_ct_effect = 20
        event_2.card_cash_wr_effect = -20
        event_2.card_approval_ct_effect = 2
        event_2.card_approval_wr_effect = -5
        event_2.save()

        # card 3
        card_3 = Card()
        card_3.card_title = "Card de Monitoramento"
        card_3.card_description = "O tempo para uma atividade foi ..."
        card_3.card_level = 1
        card_3.card_ct_choice = "correct option"
        card_3.card_wr_choice = "wrong option"
        card_3.card_image_path = ""
        card_3.save()

        # event 3
        event_3 = Event()
        event_3.card = card_1
        event_3.card_cash_ct_effect = 20
        event_3.card_cash_wr_effect = -20
        event_3.card_approval_ct_effect = 2
        event_3.card_approval_wr_effect = -5
        event_3.save()

        # game state 1
        game_state_1 = GameState()
        game_state_1.current_cash = 2500.00
        game_state_1.current_approval = 100
        game_state_1.current_client_satisfaction = 100
        game_state_1.current_employees_satisfaction = 100
        game_state_1.current_overrall_satisfaction = 100
        game_state_1.current_level = 1
        game_state_1.save()

        # user 1
        user_1 = User()
        user_1.user_name = "randomUser1"
        user_1.user_current_state = game_state_1
        user_1.save()

        return

    def test_units(self):
        print("\n======= Starting unit tests ======")

        print("\nCreating new game state ")
        tmp_game_state = create_new_game_state()
        self.assertIsInstance(tmp_game_state, GameState)

        print("\nCreate new User")
        tmp_user = create_new_user("test_user", tmp_game_state)
        self.assertIsInstance(tmp_user, User)

        print("\nGet game state")
        tmp_game_state = get_game_state(tmp_user)
        self.assertIsInstance(tmp_game_state, GameState)

        print("\nRetrieve event list")
        event_list = retrieve_event_list(1)
        for event in event_list:
            self.assertEqual(event.card.card_level,1)
        self.assertLessEqual(len(event_list),5)

        return

    def test_client_requests_handling(self):

        # Tests for client requests
        print(" ====== Initiating tests with user making requests ========")
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
        print("\nMaking request for update game state for a existing User")
        response = tmp_client.post('/cards/save_game_state/', {'username': 'new_user',
            'game_cash' : '2399.00',
            'game_approval' : '96',
            'game_cli_satis' : '92',
            'game_emp_satis' : '93',
            'game_over_satis' : '90',
            'game_level': '1'})
        self.assertEqual(response.status_code, 200)

        print("\nMaking request for update game state for a NON existing User")
        response = tmp_client.post('/cards/save_game_state/', {'username': 'other_user',
            'game_cash' : '2399.00',
            'game_approval' : '96',
            'game_cli_satis' : '92',
            'game_emp_satis' : '93',
            'game_over_satis' : '90',
            'game_level': '1'})
        self.assertEqual(response.status_code,400)

        # Requesting Event List
        print("\nMaking request for events list for an existing User")
        response = tmp_client.post('/cards/get_events/', {'game_level' : 1})
        return