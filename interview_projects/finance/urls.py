from django.urls import path
from . import views

urlpatterns = [
    path("", views.finance_view, name="index"),
    path("add_expenditure", views.add_expenditure, name="add_expenditure"),
    path("delete_expenditure/<int:item_id>", views.delete_expenditure, name="delete_expenditure"),
]
