from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks = ['asd', 'xcv', 'ewq']

def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })