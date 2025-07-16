from django.shortcuts import render,redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    else:
        form = TaskForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
def change_status(request, task_id, new_status):
    task = get_object_or_404(Task, pk=task_id)
    if new_status in Task.Status.values:
        task.status = new_status
        task.save()
    return redirect('home')
