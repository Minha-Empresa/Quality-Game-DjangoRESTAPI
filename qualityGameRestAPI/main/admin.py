from django.contrib import admin
from .models import Card, GameState, User, Event
# Register your models here.

admin.site.register(GameState)
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Event)