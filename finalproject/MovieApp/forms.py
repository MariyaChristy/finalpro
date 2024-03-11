from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie,MovieComment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','image','description']

        def __init__(self, *args, **kwargs):
            # Extract the 'user' argument from kwargs
            user = kwargs.pop('user', None)

            # Call the parent class's __init__ method
            super(MovieForm, self).__init__(*args, **kwargs)

            # Now you can use the 'user' variable as needed
            if user:
                # Do something with the user, for example, set a field in the form
                self.fields['user'].initial = user

class CommentMovieForm(forms.ModelForm):
    class Meta:
        model=MovieComment
        fields=['comment']