from django import forms

from web_1_prep.main.models import Profile


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

