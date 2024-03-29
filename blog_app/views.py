from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from blog_app.models import Author, Blog
from blog_app.forms import SignUpForm, LoginForm, BlogForm

def signupview(request):
    html = "signup.html"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, html, context)

def loginview(request):
    html = "login.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, html, context)

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def index(request):
    html = "index.html"
    data = Blog.objects.all()
    context = {'data': data}
    return render(request, html, context)

@login_required
def bloginsert(request):
    html = "blog.html"
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Blog.objects.create(
                title=data['title'],
                body=data['body'],
                author_name=data['author'],
                image=data['image']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, html, context)

@login_required
def author_detail(request, username):
    html = "author.html"
    author = Author.objects.get(username=username)
    author = request.user
    blogs = Blog.objects.filter(author_name=author)
    context = {'author': author, 'blogs': blogs}
    return render(request, html, context)