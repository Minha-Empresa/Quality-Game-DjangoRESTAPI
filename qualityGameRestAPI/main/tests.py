from django.test import TestCase
from .models import Card, User, Event, GameState

class overrallTestCase(TestCase):
    
    def setUp(self):
        gamestate = GameState()
        gamestate.current_cash = 2500.0
        gamestate.current_level = 1
        gamestate.current_approval = 100
        gamestate.current_client_satisfaction = 100
        gamestate.current_employees_satisfaction = 100
        gamestate.current_overrall_satisfaction =  100
        gamestate.save()

        card = Card()
        user = User()
        event = Event()

    def test_user_initiates_level_1(self):
        """Check if new Users start level 1"""
        pass