from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from course.models import coursedetails
# Create your models here.
from django.contrib.contenttypes.fields import GenericRelation

# student course details.
class studentcoursedetails(models.Model):
    user_id =models.CharField(max_length=6,null=True,blank=True)
    Coursedetails =models.ForeignKey("course.coursedetails", on_delete=models.DO_NOTHING,null=True)
    purchase_dt=models.CharField(max_length=10,null=True,blank=True,default=datetime.now().strftime ("%Y-%m-%d"))
    status =models.CharField(max_length=20,null=True,blank=True,default="Payment Done")
    coupon =models.CharField(max_length=20,null=True,blank=True,default="Not Applied")
    discount =models.CharField(max_length=20,null=True,blank=True,default="0%")
    finalprice =models.CharField(max_length=20,null=True,blank=True)

class studentadditionaldetails(models.Model):
    user_id =models.CharField(max_length=6,null=True,blank=True)
    address1 =models.CharField(max_length=20000,null=True,blank=True)
    address2 =models.CharField(max_length=20000,null=True,blank=True)
    country =models.CharField(max_length=40,null=True,blank=True)
    state =models.CharField(max_length=40,null=True,blank=True)
    city  =models.CharField(max_length=40,null=True,blank=True)
    zip =models.CharField(max_length=10,null=True,blank=True)
     