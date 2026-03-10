from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView
from todo.models import TodoList, Todo
# Create your views here.

class IndexView(ListView):
    model = TodoList
    template_name = "todo/todo.html"
    context_object_name = "todo_lists"


def toggle_complete(request, todo_id):
    if(request.method == 'POST'):
        todo = get_object_or_404(Todo, id=todo_id)
        todo.is_completed = not todo.is_completed
        todo.save()
        return redirect('index')
    

def delete_todo(request, todo_id):
    if(request.method == 'POST'):
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return redirect('index')
    

def add_todo(request):
    if(request.method == 'POST'):
        title = request.POST.get('title')
        todo_list_id = request.POST.get('todo_list_id')
        todo_list = get_object_or_404(TodoList, id=todo_list_id)
        Todo.objects.create(title=title, todo_list=todo_list)
        return redirect('index')
    
def add_todo_page(request):
    if(request.method == 'GET'):
        todo_lists = TodoList.objects.all()
        return render(request, 'todo/add.html', {'todo_lists': todo_lists})