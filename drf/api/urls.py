from django.urls import path
from .views import *

urlpatterns = [
    path("/login",UserView.as_view(),name="login"),
    path("home1/",HomeView.as_view(),name="home"),
    path("home1/<str:pk>",HomeView.as_view(),name="home"),
]
