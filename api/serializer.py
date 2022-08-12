from dataclasses import fields
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