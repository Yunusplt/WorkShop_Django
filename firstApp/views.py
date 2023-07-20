from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hellooo....")


def students(request):
    return HttpResponse("Hello Studentss....")
