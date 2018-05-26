from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView

def index(request):
    return render(request,"general/index.html")


