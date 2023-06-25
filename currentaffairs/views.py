from datetime import datetime
from django.shortcuts import render
from yuktmind.decorators import allowed_users
from currentaffairs.models import currentaffairdetails,currentaffairsubsription
from django.contrib.auth.decorators import login_required


@login_required(login_url="signin")
def currentaffairhome(request):
    currentaffairs=currentaffairdetails.objects.filter(c_start_dt=datetime.now().strftime ("%Y-%m-%d"))[:10]
  
    
    context ={
        'currentaffairs': currentaffairs

    }
    return render(request,"currentaffairs/index.html",context)
