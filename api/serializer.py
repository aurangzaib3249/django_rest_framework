from dataclasses import fields
import email
from turtle import mode
from xml.dom import ValidationErr
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
        
class SendEmailSerializer(serializers.Serializer):
    email=serializers.EmailField()
    class Meta:
        fields=["email"]
    
    
class changePasswordSerializer(serializers.Serializer):
    password1=models.CharField()
    password2=models.CharField()
    class Meta:
        fields=["password1","password1"]
        
    def validate(self, attrs):
        password1=attrs.get("password1")
        password2=attrs.get("password2")
        if password1 !=password2:
            raise serializers.ValidationError("Password not matched")
        
        return attrs