from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^cards/$', views.CardList.as_view(), name='card-list'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    path('get_game_state/', views.retrieve_game_state, name='game-state'),
    path('get_user/', views.create_or_retrieve_user, name='create_or_retrieve_user'),
    path('get_events/', views.get_events, name="game_events"),
    path('save_game_state/', views.save_game_state, name='save_game_state'),
]