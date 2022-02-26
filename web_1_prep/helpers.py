from web_1_prep.main.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    return profile[0]


def get_all_expenses():
    expenses = Expense.objects.all()
    return expenses