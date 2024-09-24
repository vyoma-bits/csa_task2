# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def getAllTodos(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos})

@login_required
def getTodo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        todo = Todo.objects.create(title=title, description=description, user=request.user)
        return redirect('todos:get_todos')
    return render(request,'todos/create_todo.html')

@login_required
def update(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        print(request.POST.get('completed'))
        todo.title = request.POST.get('title', todo.title)
        todo.description = request.POST.get('description', todo.description)
        todo.completed = request.POST.get('completed', todo.completed) == 'on'
        todo.save()
        return redirect('todos:get_todos')
    return render(request, 'todos/update_todo.html', {'todo': todo}) 


@login_required
def delete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todos:get_todos')
