from django.urls import path
from .views import *

urlpatterns = [
    path("login",UserView.as_view(),name="login"),
    
    path("",ConcreteGenericViews.as_view(),name="home"),
    path("<str:pk>/",ConcreteGenericViewsPk.as_view(),name="home"),
    path("list",MixinViews.as_view(),name="list"),
    path("list/<str:pk>",MixinViewsPk.as_view(),name="list"),
    
    
]
