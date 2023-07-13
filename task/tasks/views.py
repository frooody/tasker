from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session["tasks"]
    })
def add(request):
    #return render(request, "tasks/index.html")
    return HttpResponse("add")
