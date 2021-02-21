from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog_app.models import Author, Blog

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.Charfield(max_length=30)

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
