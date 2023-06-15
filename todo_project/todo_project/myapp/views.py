from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm

# Create your views here.
# def add(request):
#     task1=Task.objects.all()
#     if request.method =='POST':
#         name=request.POST.get('task','')
#         priority=request.POST.get('priority','')
#         date = request.POST.get('date', '')
#     return render(request, 'home.html')






def add(request):
    task=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('taskName', '')
        priority = request.POST.get('priority', '').title()
        date = request.POST.get('date', '')
        Task.objects.create(name=name, priority=priority, date=date)
        return redirect('/')
    return render(request, 'home.html', {'task': task})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def display(request,task_id):
    task=Task.objects.get(id=task_id)
    return render(request,'display.html',{'task':task})

# def update(request,id):
#     task=Task.objects.get(id=id)
#     f=TodoForm(request.POST or None, instance=task)
#     if f.is_valid():
#         task.priority = data['priority']
#         f.save()
#         return redirect('/')
#     return render(request,'update.html',{'f':f,'task':task})


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)

    if f.is_valid():
        data = f.cleaned_data  # Get the cleaned form data
        task.taskName = data['name'].title()  # Convert the taskName to CamelCase
        task.priority = data['priority'].title()
        task.date = data['date']
        task.save()
        return redirect('/')

    return render(request, 'update.html', {'f': f, 'task': task})
