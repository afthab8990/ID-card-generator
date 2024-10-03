from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def homepage(request):
    return render(request,'homepage.html')

def generator(request):
    return render(request,'generator.html')

    
# Create your views here.
