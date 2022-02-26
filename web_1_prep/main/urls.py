from django.urls import path

from web_1_prep.main.views.generic import show_home

urlpatterns = [
    path('', show_home, name='index')
]