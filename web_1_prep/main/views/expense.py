from django.shortcuts import render, redirect

from web_1_prep.main.forms import CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from web_1_prep.main.models import Expense


def expense_action(request, form_class, instance, success_url, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'expense': instance,
    }

    return render(request, template_name, context)


def create_expense(request):
    return expense_action(request, CreateExpenseForm, Expense(), 'index', 'expense-create.html')


def edit_expense(request, pk):
    return expense_action(request, EditExpenseForm, Expense.objects.get(pk=pk), 'index', 'expense-edit.html')


def delete_expense(request, pk):
    return expense_action(request, DeleteExpenseForm, Expense.objects.get(pk=pk), 'index', 'expense-delete.html')
