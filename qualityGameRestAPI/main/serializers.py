from rest_framework import serializers
from .models import Card, Event, User, GameState

class CardSerializer(serializers.ModelSerializer):

    class Meta:

        model = Card
        fields = '__all__'

class GameStateSerializer(serializers.ModelSerializer):

    class Meta:

        model = GameState
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Event
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'