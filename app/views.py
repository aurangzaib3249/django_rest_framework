from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Creae your views here.

@login_required(login_url="login")
def home(request):
    return render(request,"home.html")

def user_login(request):
    return render(request,"login.html")