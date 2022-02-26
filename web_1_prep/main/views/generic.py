from django.shortcuts import render, redirect

from web_1_prep.helpers import get_profile, get_all_expenses
from web_1_prep.main.forms import CreateProfileForm
from web_1_prep.main.models import Profile
from web_1_prep.main.templatetags.profiles import profiles_exist


# def show_home(request):
#     profile = get_profile()
#     # Why can't I add this as context? 'budget': budget?
#     # budget = profile.budget
#
#     if profiles_exist():
#         return render(request, 'home-with-profile.html')
#
#     else:
#         if request.method == 'POST':
#             form = CreateProfileForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return render(request, 'home-with-profile.html')
#
#         else:
#             form = CreateProfileForm()
#
#         context = {
#             'form': form,
#             'profile': profile,
#         }
#
#         return render(request, 'home-no-profile.html', context)
#


def show_home(request):

    if profiles_exist():
        profile = get_profile()
        expenses = get_all_expenses()
        leftovers = profile.budget
        for expense in expenses:
            leftovers -= expense.price

        context = {
            'profile': profile,
            'expenses': expenses,
            'leftovers': leftovers
        }

        return render(request, 'home-with-profile.html', context)

    else:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        else:
            form = CreateProfileForm()

        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)


