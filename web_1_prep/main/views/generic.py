from django.shortcuts import render

from web_1_prep.main.models import Profile
from web_1_prep.main.templatetags.profiles import profiles_exist


def show_home(request):

    if profiles_exist():
        return render(request, 'home-with-profile.html')
    else:
        return render(request, 'home-no-profile.html')


