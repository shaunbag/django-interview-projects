from django import forms
from .models import Todo, TodoList

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'todo_list']
        labels = {
            'todo_list': 'Select A Todo List'
        }