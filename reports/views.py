from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def newreport(request):
    return HttpResponse("newreport")

def savedreports(request):
    return HttpResponse("savedreports")