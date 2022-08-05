from django.urls import path
from .views import *

from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path("",Home.as_view(),name="home"),
    path('api-token-auth', obtain_auth_token, name='token'),
    path('todo', TodoList.as_view(), name='todo'),
    
]
