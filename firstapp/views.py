from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context =  {"lugat":{"ism":"Alijon","familiya":"Falonchayev"},
            'name':"Mirshod",
            'surname':"Boltayev",
            }
    return render(request, 'index.html',context)

def hello(request):
    return HttpResponse('Hello World!')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def service(request):
    return render(request, 'service.html')