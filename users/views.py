from curses.ascii import HT
import imp
from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    
    return render(request,"account/base.html")


def test(request):
    return render(request,"account/dummy.html")
