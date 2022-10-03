from http import client
from django.urls import path
from .views import (
    list_view,
    client #new function in  views.py    
)

app_name = 'main'
urlpatterns = [
    path('', list_view, name='home-list'),
    path('join-now',client, name='hangout'),#new url route
]