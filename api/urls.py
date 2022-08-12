from django.urls import path
from .views import *

urlpatterns = [
    path("login",UserView.as_view(),name="login"),
    path("",HomeView.as_view(),name="home"),
    path("<str:pk>",HomeView.as_view(),name="home"),
]
