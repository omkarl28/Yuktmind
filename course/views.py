from django.shortcuts import render
from yuktmind.decorators import allowed_users
from course.models import coursedetails,lecturedetails
from student.models import studentcoursedetails
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="signin")
def coursehome(request):
    courses=coursedetails.objects.filter() 
  
    
    context ={
        'returncourse': courses

    }
    return render(request,"course/index.html",context)

#   c_id =models.CharField(max_length=6,null=True,blank=True)
#   c_summary =models.CharField(max_length=20000,null=True,blank=True)
#   c_name=models.CharField(max_length=200,null=True,blank=True)
### c_start_dt=models.CharField(max_length=10,null=True,blank=True)
#   c_end_dt=models.CharField(max_length=10,null=True,blank=True)
#   c_fees=models.CharField(max_length=10,null=True,blank=True)
#   c_hours=models.CharField(max_length=10,null=True,blank=True)
#   c_class_detail=models.CharField(max_length=10,null=True,blank=True)
#   c_views=models.CharField(max_length=10,null=True,blank=True)
#   c_likes=models.CharField(max_length=10,null=True,blank=True)
#   c_total_seats=models.CharField(max_length=10,null=True,blank=True)
#   c_available_seats=models.CharField(max_length=10,null=True,blank=True)
#   c_category=models.CharField(max_length=20,null=True,blank=True)


#@login_required(login_url="signin")   
@allowed_users(allowed_roles=['teacher'])
def addcourse(request):
    if request.user.is_authenticated:

        if request.method=="POST":
            c_summary=request.POST.get("c_summary")
            c_name=request.POST.get("c_name")
            c_start_dt=request.POST.get("c_start_dt")
            c_end_dt=request.POST.get("c_end_dt")
            c_fees=request.POST.get("c_fees")
            c_hours=request.POST.get("c_hours")
            c_class_detail=request.POST.get("c_class_detail")
            c_total_seats=request.POST.get("c_total_seats")
            c_category=request.POST.get("c_category")
            print("c_name",c_name)

            coursedetails.objects.create(c_summary=c_summary,c_name=c_name,c_start_dt=c_start_dt,c_end_dt=c_end_dt,c_fees=c_fees,c_hours=c_hours,c_class_detail=c_class_detail,c_total_seats=c_total_seats,c_category=c_category)
         
        

    return render(request,"course/addcourse.html")


def coursedetail(request,courseid):
    courses=coursedetails.objects.filter(id=courseid) 
  
    
    context ={
        'returncourse': courses

    }
    return render(request,"course/coursedetail.html",context)

def buycourse(request,courseid):
    courses=coursedetails.objects.get(id=courseid)
    coursefees=coursedetails.objects.filter(id=courseid) 
    
    #user_id =models.CharField(max_length=6,null=True,blank=True)
    #course_id =models.CharField(max_length=20000,null=True,blank=True)
    #purchase_dt=models.CharField(max_length=10,null=True,blank=True,default=datetime.now().strftime ("%Y-%m-%d"))
    #status =models.CharField(max_length=20,null=True,blank=True,default="Payment Done")
    #coupon =models.CharField(max_length=20,null=True,blank=True,default="Not Applied")
    ##discount =models.CharField(max_length=20,null=True,blank=True,default="0%")
    #finalprice =models.CharField(max_length=20,null=True,blank=True)
    
    if request.method=="POST":
      currentuser=request.user
         
      studentcoursedetails.objects.create(user_id=currentuser.id,Coursedetails=courses,finalprice=coursefees[0].c_fees)

    context ={
        'returncourse': coursefees

    }
    return render(request,"course/purchase.html",context)

def lecture(request,courseid):
    courses=coursedetails.objects.get(id=courseid)
    coursedetailsreturn=coursedetails.objects.filter(id=courseid)
  

    lectures=lecturedetails.objects.filter(Coursedetails=courses) 
    print(lectures)
    #user_id =models.CharField(max_length=6,null=True,blank=True)
    #course_id =models.CharField(max_length=20000,null=True,blank=True)
    #purchase_dt=models.CharField(max_length=10,null=True,blank=True,default=datetime.now().strftime ("%Y-%m-%d"))
    #status =models.CharField(max_length=20,null=True,blank=True,default="Payment Done")
    #coupon =models.CharField(max_length=20,null=True,blank=True,default="Not Applied")
    ##discount =models.CharField(max_length=20,null=True,blank=True,default="0%")
    #finalprice =models.CharField(max_length=20,null=True,blank=True)
    
   
    context ={
        'lectures': lectures,
        'courses':coursedetailsreturn

    }
    return render(request,"course/lecture.html",context)