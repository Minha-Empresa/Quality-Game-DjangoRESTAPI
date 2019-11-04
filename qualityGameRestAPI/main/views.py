from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Card, User, GameState, Event
from .serializers import CardSerializer, UserSerializer, GameStateSerializer

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
            gameState = GameState()
            gameState.current_cash = 2500.00
            gameState.current_approval = 100
            gameState.current_client_satisfaction = 100
            gameState.current_employees_satisfaction = 100
            gameState.current_overrall_satisfaction = 100
            gameState.current_level = 1
            gameState.save()

            # Creating user
            user = User()
            user.user_name = request.data["username"]
            user.user_current_state = gameState
            user.save()
            return Response(UserSerializer(user).data)

        else:
            # User exists, return user data
            user = users[0]
            return Response(UserSerializer(user).data)  
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)