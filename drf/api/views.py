from functools import partial
from webbrowser import get
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.core.exceptions import ObjectDoesNotExist
from .CustomApiView import *
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView,GenericAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveDestroyAPIView,RetrieveAPIView
from rest_framework.mixins import ListModelMixin,DestroyModelMixin,UpdateModelMixin,CreateModelMixin,RetrieveModelMixin
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
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
 #Generic View 
class GenericViews(GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get(self, request, *args, **kwargs):
        data=self.get_queryset()
        serializer=self.serializer_class(data,many=True)
        serializer=serializer.data
        return  Response(serializer)
    def post(self, request, *args, **kwargs):
        data=request.data
        ser=self.serializer_class(data=data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    
class GenericViewsPk(GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get(self, request, *args, **kwargs):
        ser=UserSerializer(self.get_object())
        return Response(ser.data)
    
    def put(self, request, *args, **kwargs):
        partial=kwargs.pop("partial",False)
        user=self.get_object()
        serializer=self.serializer_class(user,data=request.data,partial=partial)
        if serializer.is_valid():
            serializer.save()
          
        else:
            return Response(serializer.errors)    
        return Response(serializer.data)
    def delete(self, request, *args, **kwargs):
        user=self.get_object()
        user.delete()
        return Response("Deleted")
    def get_object(self):
        pk=self.kwargs["pk"]
        user=User.objects.filter(id=pk).first()
        
        return user
   
class ConcreteView(ListAPIView,CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class ConcreteViewPk(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    serializer_class=UserSerializer
    queryset = User.objects.all()
    permission_classes=[IsAuthenticated]
    """def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect("login")"""
    
    

# no need pk in list and create view
class user_list(GenericAPIView,ListModelMixin,CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        
        return self.create(request,*args, **kwargs)
   

# need pk for update,delete,and retrieve    
class user_list_pk(GenericAPIView,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    lookup_field="pk"
    def delete(self,request,*args, **kwargs):
        
        return self.destroy(request,*args, **kwargs)
    def put(self,request,*args, **kwargs):
        
        return self.update(request,*args, **kwargs)
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    
class list1(GenericAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
#Generic APIView  end