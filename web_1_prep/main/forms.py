from django import forms

from web_1_prep.helpers import DisabledFormMixin
from web_1_prep.main.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # widgets={
        #     'profile_image': forms.ImageField(
        #     attrs={
        #         'class': 'form-file'
        #     }
        # )
        # }


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DeleteExpenseForm(DisabledFormMixin, forms.ModelForm):

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self._init_disable_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'
