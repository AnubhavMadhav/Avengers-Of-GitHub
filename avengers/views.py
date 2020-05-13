from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    return HttpResponse("This is gonna be Result Page")