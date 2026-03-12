from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView
from .models import TodoList, Todo
from .forms import TodoForm
from django.views.decorators.http import require_http_methods


class IndexView(ListView):
    model = TodoList
    template_name = "todo/todo.html"
    context_object_name = "todo_lists"


@require_http_methods(['POST'])
def toggle_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('index_todo')


@require_http_methods(['POST'])
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('index_todo')


@require_http_methods(['POST'])
def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index_todo')


@require_http_methods(['GET'])
def add_todo_page(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'todo/add.html', {'form': form})
