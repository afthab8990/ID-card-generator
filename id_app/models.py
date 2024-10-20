from django.db import models
from .models import *

class instituition(models.Model):
    institutionName = models.CharField(max_length=40)
    institutionAddress = models.CharField(max_length=250)
    institutionLogo = models.ImageField()
    institutionNumber = models.IntegerField()
    institutionNumber2 = models.IntegerField()
    institutionEmail = models.EmailField()
    institutionEmail2 = models.EmailField()

class student(models.Model):
    sinstitution=models.ForeignKey(instituition,on_delete=models.CASCADE)
    studentName = models.CharField(max_length=25)
    studentRollnumber = models.IntegerField()
    studentDepartment = models.CharField(max_length=50)
    studentNumber = models.IntegerField()
    studentAddress1 = models.CharField(max_length=50)
    studentAddress2 = models.CharField(max_length=50)
    studentAddress3 = models.CharField(max_length=50)
    studentPhoto = models.ImageField()
# Create your models here.
