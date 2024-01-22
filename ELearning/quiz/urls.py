from django.urls import path
from . import views

urlpatterns = [
    path('all_quiz', views.all_quiz_view, name='all_quiz'),
    path('search/<str:category>', views.searchView, name='search'),
    
]