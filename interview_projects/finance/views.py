from django.shortcuts import get_object_or_404, render, redirect  #
from .models import UserBudget, Expenditure
from .forms import ExpenditureForm
from django.views.decorators.http import require_http_methods


# Create your views here.

def index(request):
    template = 'finance/index.html'
    return render(request, template)


@require_http_methods(['GET'])
def finance_view(request):
    template = 'finance/finance.html'
    budget = UserBudget.objects.get(id=1)
    form = ExpenditureForm()
    expenditures = Expenditure.objects.all()
    current_spent = sum(item.cost for item in expenditures)
    remaining = budget.total - current_spent
    return render(request, template,
                  {"total": budget.total, "form": form, "expenditures": expenditures, "remaining": remaining})


@require_http_methods(['POST'])
def add_expenditure(request):
    form = ExpenditureForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')


@require_http_methods(['POST'])
def delete_expenditure(request, item_id):
    item = get_object_or_404(Expenditure, id=item_id)
    item.delete()
    return redirect('index')
