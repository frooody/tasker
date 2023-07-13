
from django.contrib import admin
from django.urls import path, include

app_name = 'tasks'

urlpatterns = [
    path('/tasks', include('tasks.urls')),
]
