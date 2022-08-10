from dataclasses import fields
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","password"]
       
class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude = ('password',"user_permissions","groups","is_superuser","first_name","last_name","is_staff","is_active","last_login")
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"
    

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Token
        fields="__all__"