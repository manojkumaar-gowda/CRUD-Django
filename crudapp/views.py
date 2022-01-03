from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from crudapp.models import Task
from crudapp.forms import Taskform
# Create your views here.
def home(request):
    tasksval = Task.objects.all()
    return render(request,'crudapp/index.html',{'taskskey':tasksval})

def add(request):
    form = Taskform()
    if(request.method=='POST'):
        form = Taskform(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/')
    return render(request,'crudapp/add.html',{'form':form})

def delete(request,id):
    Tasks = Task.objects.get(id=id)
    Tasks.delete()
    tasksval = Task.objects.all()
    return redirect('/')

def edit(request,id):
    tasksval = Task.objects.get(id=id)
    if(request.method=='POST'):
        form = Taskform(request.POST,instance=tasksval)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'crudapp/edit.html',{'taskskey':tasksval})