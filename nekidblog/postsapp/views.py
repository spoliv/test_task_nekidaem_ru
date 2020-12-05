from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.views.generic import ListView
from django.urls import reverse
from postsapp.forms import BlogAuthorLoginForm, PostForm
from django.contrib.auth.models import User as BlogAuthor
from .models import Blog


def login(request):
    title = 'вход'

    login_form = BlogAuthorLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            form = PostForm()
            context = {'post_form': form}
            return render(request, 'postsapp/index.html', context)
    context = {'title': title, 'login_form': login_form}
    return render(request, 'postsapp/login.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            blog = Blog.objects.filter(author=request.user).first()
            form.instance.blog = blog
            form.save()
            form = PostForm()
    else:
        form = PostForm()
    context = {'post_form': form}
    return render(request, 'postsapp/index.html', context)


class BlogList(ListView):
    template_name = "postsapp/blogs.html"
    model = Blog

    def get_queryset(self):
        return Blog.objects.all().select_related()
