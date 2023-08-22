from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "base.html")

def list(request):
    return HttpResponse("this is a vegetable")