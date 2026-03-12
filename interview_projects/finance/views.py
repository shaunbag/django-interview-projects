from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import UserBudget, Expenditure
from .forms import ExpenditureForm
# Create your views here.


def index(request):
    template = 'finance/index.html'
    return render(request, template)


def finance_view(request):
    template = 'finance/finance.html'
    budget = UserBudget.objects.get(id=1)
    form = ExpenditureForm()
    expenditures = Expenditure.objects.all()
    current_spent = sum(item.cost for item in expenditures)
    remaining = budget.total - current_spent
    return render(request, template, {"total" : budget.total, "form": form, "expenditures": expenditures, "remaining": remaining})


def add_expenditure(request):
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')        


def delete_expenditure(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Expenditure, id=item_id)
        item.delete()
        return redirect('index')