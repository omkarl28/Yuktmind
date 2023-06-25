from datetime import datetime
import re
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from course.models import *
from currentaffairs.models import *
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
def home(request):
    if request.method=="POST":
            emailid=request.POST.get("emailid")
            print("emailid",emailid)
            currentaffairsubsription.objects.get_or_create(cas_email=emailid)
    courses=coursedetails.objects.filter().order_by('-c_likes')[:3:-1]
    currentaffairs=currentaffairdetails.objects.filter(c_start_dt=datetime.now().strftime ("%Y-%m-%d"))[:10]
    context ={
        'returncourse': courses,
        'currentaffairs':currentaffairs

    }    
    return render(request,"homepage/index.html",context)



def logout_view(request):
    logout(request)
    return redirect('home')

 
 