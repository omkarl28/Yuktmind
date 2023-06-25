from http.client import HTTPResponse
from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword") 

        myuser=User.objects.create_user(username,email,password)
        User.firstname=firstname 
        User.lastname=lastname 
        myuser.save()
        messages.success(request,"Your account has been created ")
        return redirect("signin")

    return render(request,"authentication/signup.html")

def signin(request):
    if request.method=="POST":
       
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
              
                login(request, user)
                
                return redirect(request.POST.get('next','home'))
            else:
                return render(request,"authentication/signin.html")
    return render(request,"authentication/signin.html")

def signout(request):
    pass
