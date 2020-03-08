from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def info(request):
    return render(request, "complaint.html")
