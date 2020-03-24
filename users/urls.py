from django.urls import path

from . import views

app_name='users'

urlpatterns = [
    path('Login/', views.Login, name='Login'),
    path('Login_User/', views.Login_User, name='Login_User'),
    

    ]
