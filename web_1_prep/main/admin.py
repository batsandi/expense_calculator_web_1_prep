from django.contrib import admin

from web_1_prep.main.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'full_name'
    ]


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'pk',
        'price'
    ]
