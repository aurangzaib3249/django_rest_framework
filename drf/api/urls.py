from django.urls import path
from .views import *

urlpatterns = [
    path("login",UserView.as_view(),name="login"),
    path("token",GetToken.as_view(),name="token"),
    path("",List.as_view(),name="auth"),
    path("<str:pk>/",Edit.as_view(),name="auth"),
    #path("",HomeView.as_view(),name="home"),
    #path("<str:pk>",HomeView.as_view(),name="home"),
]
