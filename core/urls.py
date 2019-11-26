from django.urls import path
from django.contrib import admin
from .views import home,login,logout,register
from core import views
urlpatterns = [
    path('',home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout/', logout, name='logout'),

   
]
