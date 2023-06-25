from django.db import models
from datetime import datetime

# Create your models here.
# current affair  Details.
class currentaffairdetails(models.Model):
    ca_id =models.CharField(max_length=6,null=True,blank=True)
    ca_link =models.CharField(max_length=20000,null=True,blank=True)
    ca_text=models.CharField(max_length=200,null=True,blank=True)
    c_start_dt=models.CharField(max_length=10,null=True,blank=True,default=datetime.now().strftime ("%Y-%m-%d"))

# current affair  subsription.
class currentaffairsubsription(models.Model):
    cas_id =models.CharField(max_length=6,null=True,blank=True)
    cas_email =models.CharField(max_length=20000,null=True,blank=True)
    cas_start_dt=models.CharField(max_length=10,null=True,blank=True,default=datetime.now().strftime ("%Y-%m-%d"))
     