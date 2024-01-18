from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('allquiz/', views.takeQuiz, name='takeQuiz'),
    path('quiz/', views.quiz, name='quiz'),

]