from django.urls import path
from .views import *

urlpatterns = [
    path("login",UserView.as_view(),name="login"),
    #path("",HomeView.as_view(),name="home"),
    #path("<str:pk>",HomeView.as_view(),name="home"),
    
    path("UserList/",user_list.as_view(),name="user_list"),
    path("UserListPk/<str:pk>",user_list_pk.as_view(),name="user_list"),
    path("",ConcreteView.as_view(),name="generic_list"),
    path("<str:pk>",ConcreteViewPk.as_view(),name="generic_list_pk"),
    path("views/",GenericViews.as_view(),name="generic_list_pk"),
    path("views/<str:pk>",GenericViewsPk.as_view(),name="generic_list_pk"),
]
