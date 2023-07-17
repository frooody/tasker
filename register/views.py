from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your iews here.
from .forms import NewUserForm

def index(request):
    form = NewUserForm()
    context = {"form": form}
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'register/register.html', context)