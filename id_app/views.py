from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def homepage(request):
    return render(request,'homepage.html')

def generator(request):
    return render(request,'generator.html')

def institutions(request):
    idata = instituition.objects.all()
    return render(request,'institutions.html',{'idata':idata})

def addinstitutions(request):
    return render(request,'addinstitutions.html')

def postinstitutions(request):
    if request.method=='POST':
        institutionName = request.POST['institutionName']
        institutionAddress = request.POST['institutionAddress']
        institutionLogo = request.FILES['institutionLogo']
        institutionNumber = request.POST['institutionNumber']
        institutionNumber2 = request.POST['institutionNumber2']
        institutionEmail = request.POST['institutionEmail']
        institutionEmail2 = request.POST['institutionEmail2']
        data = instituition(institutionName=institutionName,institutionAddress=institutionAddress,institutionLogo=institutionLogo,institutionNumber=institutionNumber,institutionNumber2=institutionNumber2,institutionEmail=institutionEmail,institutionEmail2=institutionEmail2)
        data.save()
    return redirect('institutions')

def editinstitutions(request,id):
    data = instituition.objects.filter(id=id)
    return render(request,'editinstitutions.html',{'data':data})


# Create your views here.
