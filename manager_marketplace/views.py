from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'manager_marketplace/paginas/index.html')

def home(request):
    return render(request,'manager_marketplace/paginas/home.html')
