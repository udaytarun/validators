from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import*

def student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sage=SFDO.cleaned_data['Sage']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']
            mobile=SFDO.cleaned_data['mobile']
            SO=Student.objects.get_or_create(Sname=Sname,Sage=Sage,Semail=Semail,Sid=Sid,mobile=mobile)[0]
            SO.save()
            QSSO=Student.objects.all()
            d1={'QSSO':QSSO}
            return render(request,'display.html',d1)


        else:
            return HttpResponse('Invalid data')

    return render(request,'student.html',d)

def display(request):
    QSSO=Student.objects.all()
    d={'QSSO':QSSO}
    return render(request,'display.html',d)


