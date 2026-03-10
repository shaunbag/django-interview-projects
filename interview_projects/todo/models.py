from django.db import models
from django.urls import reverse

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("todo_detail", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return self.title