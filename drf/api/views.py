from turtle import RawTurtle
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import login,authenticate
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .serializer import *
from .models import *
from rest_framework import authentication,permissions
from django.core.exceptions import ObjectDoesNotExist
from .CustomApiView import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import *
# Create your views here.


class Home(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        content={'message': 'Home'}
        return Response(content)
    
class TodoList(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        list=Todo.objects.all()
        list=TodoSerializer(list,many=True)
        data=list.data
        return Response(data)