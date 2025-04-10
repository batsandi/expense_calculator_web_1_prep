from django.urls import path

from web_1_prep.main.views.expense import create_expense, edit_expense, delete_expense
from web_1_prep.main.views.generic import show_home
from web_1_prep.main.views.profile import show_profile, delete_profile, edit_profile

urlpatterns = [
    path('', show_home, name='index'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),
    path('profile/', show_profile, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]