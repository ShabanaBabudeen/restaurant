from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def search(request):
    return render(request,'search.html')