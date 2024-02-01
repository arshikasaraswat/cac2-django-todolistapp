from django.shortcuts import render, redirect
from .models import Task
# todo_app/views.py
from user_activity.models import UserActivity

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description)
        UserActivity.objects.create(user=request.user, activity_type='Task Created', task=task)
        return redirect('task_list')
    return render(request, 'todo_app/add_task.html')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    UserActivity.objects.create(user=request.user, activity_type='Task Completed', task=task)
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    UserActivity.objects.create(user=request.user, activity_type='Task Deleted', task=task)
    return redirect('task_list')

