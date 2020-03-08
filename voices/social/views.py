from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def info(request):
    description = "Hello Worl pls im hungry"
    return render(request, "complaint.html", {
        "description": description,
    })
