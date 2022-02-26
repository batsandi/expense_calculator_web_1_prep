from django.shortcuts import render


def show_profile(request):
    return render(request, 'profile.html')


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')