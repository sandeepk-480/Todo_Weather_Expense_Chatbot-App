from django.shortcuts import render
from todo.models import TodoApp
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def todoView(request):
    data = TodoApp.objects.all()
    return render(request, 'todo/todo.html', {'tasks': data})


def add_data(request):
    if request.method == 'POST':
        data = request.POST.get('input')
        if data == '':
            messages.error(request, "Enter Task name")
        else:
            insert_data = TodoApp(name=data)
            insert_data.save()
            messages.success(request, "Task Added Successfully")
        return redirect(reverse('todo'))
    else:
        return redirect(reverse('todo'))


def delete_data(request, pk):
    data = TodoApp.objects.get(id=pk)
    data.delete()
    messages.success(request, "Task data Deleted Successfully")
    return redirect(reverse('todo'))

def finish(request, pk):
    data = TodoApp.objects.get(id=pk)
    data.status = 'Finished'
    data.save()
    return redirect(reverse('todo'))
