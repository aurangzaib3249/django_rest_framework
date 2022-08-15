from base64 import urlsafe_b64decode
from codecs import utf_16_be_decode
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
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.encoding import force_bytes,smart_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Create your views here.
from django.contrib.auth.hashers import check_password

class HomeView(APIView):
    permission_classes = [IsAuthenticated]
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
    

    
class UserProfiles(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk=None):
        user=UserSerializer(request.user)
        print(user.data)
        return Response(user.data)
class RestPassword(APIView):
    def post(self,request):
        try:
            data=request.data
            if data["email"]:
                sdata=SendEmailSerializer(data=data)
                if sdata.is_valid():
                    email=data["email"]
                    user=User.objects.filter(email=email).first()
                    if user:
                        uid=urlsafe_base64_encode(force_bytes(user.id))
                        token=PasswordResetTokenGenerator().make_token(user)
                        password_reset_link="http://127.0.0.1:8000/changePassword/"+uid+"/"+token+"/"
                        print(password_reset_link)
                        return Response(password_reset_link)
                    else:
                        return Response("email not exist")
                else:
                    return Response(sdata.errors)
            else:
                return Response("Email requied")
        except KeyError:
            return Response("Email is required")
        
class changePassword(APIView):
    def post(self,request,uid,token):
        try:
            data=request.data
            if data["password1"]!=data["password2"]:
                return Response("Password not matched")
            id=smart_str(urlsafe_base64_decode(uid))
            user=User.objects.filter(id=id).first()
            valid=PasswordResetTokenGenerator().check_token(user,token)
            print(user,valid)
            if user and  valid:
                dataserializer=changePasswordSerializer(data=data)
                if dataserializer.is_valid(raise_exception=True):
                    password=data["password1"]
                    user.set_password(password)
                    user.save()
                    return Response("set Password")
                else:
                    return Response(data.errors)
            else:
                return Response("User not found or link expired")
        except Exception as ex:
            return Response("ex",ex)
    
class ChangePasswordWithOldPassword(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,id=None):
        data=request.data
        if data:
            print(data)
            old=data["old"]
            user=authenticate(username=request.user.email,password=old)
            print(user)
            print( check_password(old, request.user.password))
            if user:
                if data["password1"]!=data["password2"]:
                    return Response("Password not matched")
                else:
                    
                    user.set_password(data["password1"])
                    user.save()
                    return Response("Your new password is set")
            else:
                return Response("Your password is wrong enter correct password or try to reset with email")
        else:
            return Response("Old,password and confirm password is required")