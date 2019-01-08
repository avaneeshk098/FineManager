from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django import forms
from django.template.defaultfilters import default



# Create your models here.
class ManagerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50, default="")
    last_name = models.CharField(max_length = 50, default = "")
    def __str__(self):
        return self.first_name
    
class Fine(models.Model):
    employee_id = models.CharField(max_length = 50, default = "")
    employee = models.CharField(max_length = 50, null = True)
    fine = models.IntegerField()
    date_applied = models.DateField(default = timezone.now)
    reason = models.TextField(default = " ") 
    def __str__(self):
        return self.employee
    
class EmployeeUser(models.Model):
    employee_id = models.CharField(max_length = 50, default = "")
    name = models.CharField(max_length = 100, default = " ")
    def __str__(self):
        return self.employee_id
    
    

    
   
    

    
    
    
    
    