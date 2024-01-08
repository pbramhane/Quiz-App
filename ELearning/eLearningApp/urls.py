from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allquiz/', views.takeQuiz, name='takeQuiz'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('quiz/', views.quiz, name='quiz'),
    path('login/', views.userlogin, name='login')
]