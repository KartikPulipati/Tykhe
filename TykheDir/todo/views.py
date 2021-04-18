from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginuser')
def listTodo(request):
    todo = Todo.objects.filter(user=request.user).order_by('due')
    return render(request, 'todo/listTodo.html', {'form': TodoForm(), 'todo': todo})

@login_required(login_url='loginuser')
def createTodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createTodo.html', {'form': TodoForm()})
    else:
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('listTodo')

@login_required(login_url='loginuser')
def deleteTodo(request, todo_pk):
    todo=get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('listTodo')
