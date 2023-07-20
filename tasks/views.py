from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.

tasks = ['asd', 'xcv', 'ewq']

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    return render(request, 'tasks/index.html')
def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        pass
    return render(request, 'tasks/add.html')