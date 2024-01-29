from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('search_users/', views.search_users, name='search_users'),

]