from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "base.html")

def list(request):
    return render(request, "list.html")

def forecast(request):
    return render(request, "forecast.html")

def todays_tasks(request):
    return render(request, "todays-tasks")