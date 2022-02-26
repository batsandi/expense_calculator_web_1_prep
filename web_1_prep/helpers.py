from web_1_prep.main.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    return profile[0]


def get_all_expenses():
    expenses = Expense.objects.all()
    return expenses


class DisabledFormMixin:
    # Override this method in child form with a tuple of fields e.g. ('name', 'age') to disable only those
    disabled_fields = '__all__'
    fields = {}

    def _init_disable_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = True
