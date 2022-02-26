from django.shortcuts import render


def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request, pk):
    return render(request, 'expense-edit.html')


def delete_expense(request, pk):
    return render(request, 'expense-delete.html')