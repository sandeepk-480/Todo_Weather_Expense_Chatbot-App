from django.shortcuts import render
from expense.models import Expense
from expense.forms import ExpenseForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


def expenseView(request):
    expense = Expense.objects.all()
    form = ExpenseForm()
    return render(request, 'expense/expense.html', {'expense':expense, 'form':form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data added Successfully")
            return redirect(reverse('expense'))
    else:
        return redirect(reverse('expense'))
    
    # return render(request, 'expense/expense.html', {'form':form})

def delete(request, pk):
    data = Expense.objects.get(id=pk)
    data.delete()
    messages.success(request, "Data Deleted Successfully")
    return redirect(reverse('expense'))