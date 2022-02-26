from django.shortcuts import render


def show_home(request):
    return render(request, 'home-no-profile.html')