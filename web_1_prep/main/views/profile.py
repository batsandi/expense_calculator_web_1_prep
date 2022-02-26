from django.shortcuts import render

from web_1_prep.helpers import get_profile


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')