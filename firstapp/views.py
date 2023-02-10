from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_control(request):
    return HttpResponse("Hello Bro! How are you?")