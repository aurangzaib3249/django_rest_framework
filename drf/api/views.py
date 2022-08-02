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
# Create your views here.

class HomeView(APIView):
    permission_classes=[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,pk=None):
        if pk:
            todo=Todo.objects.filter(id=pk)
            serializer=TodoSerializer(todo,many=True)
            return JsonResponse(
                {
                    "Data":serializer.data,
                    "Count":todo.count()
                }
            )
        else:
            todo=Todo.objects.all()
            serializer=TodoSerializer(todo,many=True)
            return JsonResponse(
                {
                    "Data":serializer.data,
                    "Count":todo.count()
                }
            )
    def post(self,request):
        try:
            data=request.data
            obj=TodoSerializer(data=data)
            if obj.is_valid():
                obj.save()
                return JsonResponse(
                    {
                        "Status":200,
                        "Message":"Task created",
                        "Data":obj.data
                    }
                )
            else:
                return JsonResponse(
                    {
                        "Status":400,
                        "Message":"Error",
                        "Data":obj.errors
                    }
                )
        except Exception as ex:
            return JsonResponse(
                    {
                        "Status":400,
                        "Message":"Error",
                        "Data":ex
                    }
                )
    def delete (self,request,pk=None):
        if pk:
            try:
                obj=Todo.objects.filter(id=pk)
                if obj:
                    
                    obj.delete()
                else:
                    return JsonResponse(
                    {
                        "Status":200,
                        "Message":"Success",
                        "Data":"Task not found"
                    }
                )
                return JsonResponse(
                    {
                        "Status":200,
                        "Message":"Success",
                        "Data":"Task deleted"
                    }
                )
            except ObjectDoesNotExist:
                return JsonResponse(
                    {
                        "Status":400,
                        "Message":"Error",
                        "Data":"Task not found with this id"
                    }
                )
                
        else:
            return JsonResponse(
                    {
                        "Status":400,
                        "Message":"Error",
                        "Data":"Task id is required"
                    }
                )
    def patch (self,request,pk=None):
        if pk:
            try:
                data=request.data
                status=data["status"]
                title=data["title"]
                obj=Todo.objects.filter(id=pk).update(title=title,status=status)
                
                
                return JsonResponse(
                    {
                        "Status":200,
                        "Message":"Success",
                        "Data":"Task Updated"
                    }
                )
            except ObjectDoesNotExist:
                return JsonResponse(
                    {
                        "Status":400,
                        "Message":"Error",
                        "Data":"Task not found with this id"
                    }
                )
        else:
            return JsonResponse(
                    {
                        "Status":400,
                        "Message":"Error",
                        "Data":"Task id is required"
                    }
                )
    
class UserView(FieldCheckView):
    
    required_params=['email','password']
    def post(self,request): 
        try:
            data=request.data
            email=data["email"]
            password=data["password"]
            if not email:
                return JsonResponse({
                    "Status":400,
                    "Message":"Email is requied"
                })
            elif not password:
                return JsonResponse({
                    "Status":400,
                    "Message":"password is requied"
                })
            else:
                user=authenticate(username=email,password=password)
                user=UserSerializer(user)
                data=user.data
                token,_=Token.objects.get_or_create(user__id=data["id"])
                data["token"]=str(token.key)
                data.pop("password")
                if user:
                    return JsonResponse({
                    "Status":400,
                    "Message":"login successfully",
                    "data": data
                })
                else:
                    return JsonResponse({
                        "Status":400,
                        "Message":"Wrong username and password"
                    })
        except KeyError as key:
            print(key)
            return JsonResponse({
                        "Status":400,
                        "Message":"{} field is required".format(key)
                    })
    def get(self,request):
        return JsonResponse({"Message":"Valid"})
    