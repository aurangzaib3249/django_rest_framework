from django.urls import path
from .views import *

urlpatterns = [
    path("login",Auth.as_view(),name="login"),
    path("home/",HomeView.as_view(),name="home"),
    path("home/<str:pk>",HomeView.as_view(),name="home"),
    path("",TodoList.as_view(),name="home"),
    path("<str:pk>/",TodoListPk.as_view(),name="home"),
]
