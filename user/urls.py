from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile')
]