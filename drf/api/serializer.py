from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"
        
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"
        
class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemCategory
        fields="__all__"
        
class CoupenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupen
        fields="__all__"
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields="__all__"