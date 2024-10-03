from django.db import models
from .models import *

class instituition(models.Model):
    instituitionName = models.CharField(max_length=40)
    instituitionAddress = models.CharField(max_length=250)
    instituitionLogo = models.ImageField()
    instituitionNumber = models.IntegerField()
    instituitionNumber2 = models.IntegerField()
    instituitionEmail = models.EmailField()
    instituitionEmail2 = models.EmailField()

class student(models.Model):
    studentName = models.CharField(max_length=25)
    studentRollnumber = models.IntegerField()
    studentNumber = models.IntegerField()
    studentAddress1 = models.CharField(max_length=50)
    studentAddress2 = models.CharField(max_length=50)
    studentAddress3 = models.CharField(max_length=50)
    studentPhoto = models.ImageField()
# Create your models here.
