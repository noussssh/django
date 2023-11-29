from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'website/welcome.html', {"message": "Message from view"})

def date(request):
    return HttpResponse("Current time : " + str(datetime.now()))

def about(request):
    return HttpResponse("This is a about page of my website")