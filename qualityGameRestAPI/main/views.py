from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Card, User, GameState, Event
from .serializers import CardSerializer, UserSerializer

# Create your views here.
class CardList(generics.ListCreateAPIView):

    queryset = Card.objects.all()
    serializer_class = CardSerializer

class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

# Example Function
@api_view(['GET', 'POST'])
def cards_list(request):
    """
    List all cards.
    """
    if request.method == 'POST':
        print("Request is post")
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

# Example Function
def users_list(request):
    """
    List all users.
    """
    if request.method == "POST":
        print("Request is post")
        users = User.objects.all()
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def create_or_retrieve_user(request):
    """
    Try to retrieve an user or create a new one
    """
    if request.method == "POST":
        print("\n\nCreate or Retrieving user with POST request")
        user = request.data["username"]

        users = User.objects.filter(user_name=user)

        if(len(users) == 0):
            print("User no exists")
            pass
        else:
            print("User found")
        return Response(status=status.HTTP_400_BAD_REQUEST)