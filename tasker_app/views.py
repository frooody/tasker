from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")
def reg(request):
    return render(request, "hello/reg.html")