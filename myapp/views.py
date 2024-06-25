from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    val1 = int(request.POST['grade1'])
    val2 = int(request.POST['grade2'])
    res = val1 + val2

    return render(request,'result.html', {'result':res})

