from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'mainmenu.html')