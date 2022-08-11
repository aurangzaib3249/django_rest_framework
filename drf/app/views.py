from contextlib import redirect_stderr
from http.client import HTTPResponse

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
@login_required(login_url="/user-login")
def home(request):
    return render(request,"main.html")

def login(request):
    return render(request,"index.html")

def logout_user(request):
    logout(request)
    return redirect("login")