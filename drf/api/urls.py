from django.urls import path
from .views import *

urlpatterns = [
    path("login",UserView.as_view(),name="login"),
    #path("",HomeView.as_view(),name="home"),
    #path("<str:pk>",HomeView.as_view(),name="home"),
    path("",Items.as_view(),name="item"),
    path("item-category",ItemCate.as_view(),name="item_category"),
    path("item-category/<str:pk>",ItemCatePk.as_view(),name="item_category"),
    path("order",ItemOrder.as_view(),name="item_category"),
    path("order/<str:pk>",ItemOrderPk.as_view(),name="item_category"),
    path("orderitem",ItemOrderItem.as_view(),name="item_category"),
    path("orderitem",ItemOrderItemPk.as_view(),name="item_category"),
    path("list",list,name="list"),
    
]
