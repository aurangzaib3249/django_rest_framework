from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Creae your views here.
from django.contrib.auth import login,authenticate,logout

@login_required()
def home(request):
    
    return render(request,"home.html")

def user_login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(email,password)
        user=authenticate(username=email,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect("home")
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect("accounts/login")