from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Creae your views here.

@login_required()
def home(request):
    return render(request,"home.html")

def user_login(request):
    return render(request,"login.html")