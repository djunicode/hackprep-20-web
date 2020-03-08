from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm

def index(request):
    complaints = Complaint.objects.all()
    return render(request, "index.html", {
        "complaints": complaints,
    })

def submit_complaint(request):
    if request.method == 'GET':
        return render(request, "complaint.html", {
            "form": ComplaintForm,
        })
    else:
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
