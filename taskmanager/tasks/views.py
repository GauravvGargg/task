from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.forms import modelform_factory
from .models import Task
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

def user_login(request):
    msg = ""
    if request.method == "POST":
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        user = authenticate(username=userid, password=password)
        if user:
            login(request, user)
            return redirect('task-list')
        else:
            msg = "Invalid credentials"
    return render(request, 'login.html', {'msg': msg})



def register(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            msg = "Passwords do not match"
        elif User.objects.filter(username=username).exists():
            msg = "Username already taken"
        else:
            user = User.objects.create_user(username=username, password=password1)
            return redirect('login')
    return render(request, 'register.html', {'msg': msg})


from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import render, redirect

@login_required
def add_task(request):
    msg = ""
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        remarks = request.POST.get('remarks')

        # Basic validation
        if not title or not due_date or not status:
            msg = "Please fill in all required fields."
        else:
            task = Task(
                title=title,
                description=description,
                due_date=due_date,
                status=status,
                remarks=remarks,
                created_by=request.user,
                updated_by=request.user
            )
            task.save()
            return redirect('task-list')

    return render(request, 'task_form.html', {'msg': msg})

@login_required
def edit_task(request, pk):
    task = Task.objects.get(pk=pk, created_by=request.user)
    msg = ""
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        remarks = request.POST.get('remarks')

        if not title or not due_date or not status:
            msg = "Please fill required fields."
        else:
            task.title = title
            task.description = description
            task.due_date = due_date
            task.status = status
            task.remarks = remarks
            task.updated_by = request.user
            task.save()
            return redirect('task-list')

    return render(request, 'task_form.html', {'task': task, 'msg': msg})






@login_required
def task_list(request):
    tasks = Task.objects.filter(created_by=request.user)
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)
    return render(request, 'task_list.html', {'tasks': tasks})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'confirm_delete.html', {'task': task})