from django.db import models

# Course Details.
class coursedetails(models.Model):
    c_id =models.CharField(max_length=6,null=True,blank=True)
    c_summary =models.CharField(max_length=20000,null=True,blank=True)
    c_name=models.CharField(max_length=200,null=True,blank=True)
    c_start_dt=models.CharField(max_length=10,null=True,blank=True)
    c_end_dt=models.CharField(max_length=10,null=True,blank=True)
    c_fees=models.CharField(max_length=10,null=True,blank=True)
    c_hours=models.CharField(max_length=10,null=True,blank=True)
    c_class_detail=models.CharField(max_length=10,null=True,blank=True)
    c_views=models.CharField(max_length=10,null=True,blank=True)
    c_likes=models.CharField(max_length=10,null=True,blank=True)
    c_total_seats=models.CharField(max_length=10,null=True,blank=True)
    c_available_seats=models.CharField(max_length=10,null=True,blank=True)
    c_category=models.CharField(max_length=20,null=True,blank=True)
        
       

# Lecture/Sections Details.
class lecturedetails(models.Model):
    l_id =models.CharField(max_length=6,null=True,blank=True)
    Coursedetails =models.ForeignKey("coursedetails", on_delete=models.CASCADE,null=True)
    l_name=models.CharField(max_length=200,null=True,blank=True)
    l_dt=models.DateTimeField(blank=True)
    t_id=models.CharField(max_length=6,null=True,blank=True)
    l_duration=models.CharField(max_length=10,null=True,blank=True)
    l_title=models.CharField(max_length=200,null=True,blank=True)
    l_download_link=models.CharField(max_length=2000,null=True,blank=True)
    l_videos=models.CharField(max_length=2000,null=True,blank=True)
    l_zoom_meet=models.CharField(max_length=3000,null=True,blank=True)
 