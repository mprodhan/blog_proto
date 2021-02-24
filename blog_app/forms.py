from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog_app.models import Author, Blog

class SignUpForm(UserCreationForm):
    author = forms.CharField(max_length=30)

    class Meta:
        model = Author
        fields = ('author', 'username', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class BlogForm(forms.Form):
    title = forms.CharField(max_length=30)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
