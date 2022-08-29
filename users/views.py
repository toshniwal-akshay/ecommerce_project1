from django.shortcuts import render 

def index(request):
    return render(request,"account/base.html")

def test(request):
    return render(request,"account/dummy.html")
