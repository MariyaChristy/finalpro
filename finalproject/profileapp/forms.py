from django import forms
from MovieApp.models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'date_of_birth', 'location']
