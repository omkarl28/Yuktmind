from django.shortcuts import render
from course.models import coursedetails
from student.models import studentcoursedetails


# Create your views here.
 
def studenthome(request):
    currentuser=request.user
 
    studentcourse=studentcoursedetails.objects.filter(user_id=currentuser.id).select_related()
   
    
  
    
    context ={
        'returncourse': studentcourse

    }
    return render(request,"student/index.html",context)

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

