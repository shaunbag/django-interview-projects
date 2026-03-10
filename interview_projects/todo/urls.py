from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("toggle_complete/<int:todo_id>/", views.toggle_complete, name="toggle_complete"),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('add_todo_page/', views.add_todo_page, name='add_todo_page'),
]
