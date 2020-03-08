from django.shortcuts import render
from .models import Complaint

def index(request):
    complaints = Complaint.objects.all()
    return render(request, "index.html", {
        "complaints": complaints,
    })

def info(request):
    description = "Hello Worl pls im hungry"
    return render(request, "complaint.html", {
        "description": description,
    })
