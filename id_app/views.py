from django.shortcuts import render,redirect, get_object_or_404
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

def updateinstitution(request,id):
    if request.method == 'POST':
        institutionName = request.POST.get('institutionName')
        institutionAddress = request.POST.get('institutionAddress')
        institutionNumber = request.POST.get('institutionNumber')
        institutionNumber2 = request.POST.get('institutionNumber2')
        institutionEmail = request.POST.get('institutionEmail')
        institutionEmail2 = request.POST.get('institutionEmail2')
        try:
            img_c = request.FILES['institutionLogo']
            fs = FileSystemStorage()
            institutionLogo = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            institutionLogo = instituition.objects.get(id=id).institutionLogo
        instituition.objects.filter(id=id).update(institutionName=institutionName,institutionAddress=institutionAddress,institutionLogo=institutionLogo,institutionNumber=institutionNumber,institutionNumber2=institutionNumber2,institutionEmail=institutionEmail,institutionEmail2=institutionEmail2)
    return redirect('institutions')

def students(request):
    sdata = student.objects.all()
    return render(request,'students.html',{'sdata':sdata})

def addstudents(request):
    idata = instituition.objects.all()
    return render(request,'addstudents.html',{'idata':idata})

def poststudents(request):
    if request.method=='POST':
        sinstitutionName = request.POST['sinstitution']
        studentName = request.POST['studentName']
        studentPhoto = request.FILES['studentPhoto']
        studentNumber = request.POST['studentNumber']
        studentRollnumber = request.POST['studentRollnumber']
        studentAddress1 = request.POST['studentAddress1']
        studentAddress2 = request.POST['studentAddress2']
        studentAddress3 = request.POST['studentAddress3']
        sinstitution = get_object_or_404(instituition, institutionName=sinstitutionName)
        data = student(sinstitution=sinstitution,studentName=studentName,studentPhoto=studentPhoto,studentNumber=studentNumber,studentRollnumber=studentRollnumber,studentAddress1=studentAddress1,studentAddress2=studentAddress2,studentAddress3=studentAddress3)
        data.save()
    return redirect('students')

def editstudents(request,id):
    data = student.objects.filter(id=id)
    idata = instituition.objects.all()
    return render(request,'editstudents.html',{'data':data,'idata':idata})

def updatestudents(request,id):
    if request.method == 'POST':
        sinstitutionName = request.POST.get('sinstitution')
        studentName = request.POST.get('studentName')
        studentPhoto = request.FILES.get('studentPhoto')
        studentNumber = request.POST.get('studentNumber')
        studentRollnumber = request.POST.get('studentRollnumber')
        studentAddress1 = request.POST.get('studentAddress1')
        studentAddress2 = request.POST.get('studentAddress2')
        studentAddress3 = request.POST.get('studentAddress3')
        try:
            img_c = request.FILES['studentPhoto']
            fs = FileSystemStorage()
            studentPhoto = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            studentPhoto = student.objects.get(id=id).studentPhoto
        sinstitution = get_object_or_404(instituition, institutionName=sinstitutionName)
        student.objects.filter(id=id).update(sinstitution=sinstitution,studentName=studentName,studentPhoto=studentPhoto,studentNumber=studentNumber,studentRollnumber=studentRollnumber,studentAddress1=studentAddress1,studentAddress2=studentAddress2,studentAddress3=studentAddress3)
    return redirect('students')

# Create your views here.
