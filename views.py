


from django.http import HttpResponse
from django.shortcuts import render


def entry(request):
    #return HttpResponse("hello navigation")
    return render(request,'entry.html')

def index(request):
    #return HttpResponse("hello navigation")
    return render(request,'index.html')


def social(request):
    #return HttpResponse("hello navigation")
    return render(request,'social.html')