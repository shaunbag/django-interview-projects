from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView
from .models import TodoList, Todo
from .forms import TodoForm


class IndexView(ListView):
    model = TodoList
    template_name = "todo/todo.html"
    context_object_name = "todo_lists"


def toggle_complete(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.is_completed = not todo.is_completed
        todo.save()
        return redirect('index')
    

def delete_todo(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return redirect('index')
    

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('index')


def add_todo_page(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'todo/add.html', {'form': form})