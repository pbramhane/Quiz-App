from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('deleteProfile/', views.deleteProfile, name='deleteProfile'),
]