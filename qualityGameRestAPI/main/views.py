from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Card, User, GameState, Event
from .serializers import CardSerializer, UserSerializer, GameStateSerializer, EventSerializer
import random
import json

# Create your views here.
class CardList(generics.ListCreateAPIView):

    queryset = Card.objects.all()
    serializer_class = CardSerializer

class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

###### Retrieve game state for user ######
@api_view(['GET', 'POST'])
def retrieve_game_state(request):
    user = request.data["username"]
    try:
        user_tmp = User.objects.get(user_name=user)
        gameState = get_game_state(user_tmp)
        if(gameState == None):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(GameStateSerializer(gameState).data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
# get game state for a given usere
def get_game_state(user_tmp):
    try:
        gameState = GameState.objects.get(pk=user_tmp.user_current_state.pk)
        return gameState
    except:
        return None

###### Create or Retrieve user information and game state ######
@api_view(['GET', 'POST'])
def create_or_retrieve_user(request):
    if request.method == "POST":
        # create or retrieve user information and game state
        user = request.data["username"]

        users = User.objects.filter(user_name=user)

        if(len(users) == 0):
            # User doesn't exists, create a new game state and a new user
            # Creating game state for the new user
            gameState = create_new_game_state()

            # Creating user
            user = create_new_user(user, gameState)

            return Response(UserSerializer(user).data)

        else:
            # User exists, return user data
            user = users[0]
            return Response(UserSerializer(user).data)  
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def create_new_game_state():
    try:
        gameState = GameState()
        gameState.current_cash = 2500.00
        gameState.current_approval = 100
        gameState.current_client_satisfaction = 100
        gameState.current_employees_satisfaction = 100
        gameState.current_overrall_satisfaction = 100
        gameState.current_level = 1
        gameState.save()
        return gameState
    except:
        return False

def create_new_user(username, gameState):
    user = User()
    user.user_name = username
    user.user_current_state = gameState
    user.save()
    return user

@api_view(['GET', 'POST'])
def save_game_state(request):
    try:
        user = request.data["username"]
        game_cash = request.data["game_cash"]
        game_approval = request.data["game_approval"]
        game_client_satisfaction = request.data["game_cli_satis"]
        game_employees_satisfaction = request.data["game_emp_satis"]
        game_overrall_satisfaction = request.data["game_over_satis"]
        game_current_level = request.data["game_level"]

    except:
        # POST data incorrect
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        user_tmp = User.objects.get(user_name=user)
    
    except:
        # User with username not found
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        gameState = GameState.objects.filter(pk=user_tmp.user_current_state.pk)
        gameState.update(current_cash=game_cash)
        gameState.update(current_approval=game_approval)
        gameState.update(current_client_satisfaction=game_client_satisfaction)
        gameState.update(current_employees_satisfaction=game_employees_satisfaction)
        gameState.update(current_overrall_satisfaction=game_overrall_satisfaction)
        gameState.update(current_level=game_current_level)
        
        return Response(GameStateSerializer(gameState[0]).data)

    except:
        # Game state not found for the given user or not updated.
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'POST'])
def get_events(request):
    level = request.data["game_level"]
    event_list = retrieve_event_list(level)
    json_response = {}
    for event in event_list:
        json_response[event.pk] = EventSerializer(event).data
        card = Card.objects.get(pk=event.card.pk)
        json_response[event.pk]["card"] = CardSerializer(card).data
    json_response = json.dumps(json_response)
    return Response(json_response)

def retrieve_event_list(level):
    events = Event.objects.all().order_by('?')
    response = []
    for event in events:
        if len(response) < 5 and event.card.card_level==int(level):
            response.append(event)
    return response
