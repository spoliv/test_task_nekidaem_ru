from django.shortcuts import render
from django.contrib import auth
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from postsapp.forms import BlogAuthorLoginForm, PostForm
from .models import Blog, Post
from subscriptionsapp.models import Subscription
from .utils import send_newpost_mail


# def login(request):
#     title = 'вход'
#
#     login_form = BlogAuthorLoginForm(data=request.POST)
#     if request.method == 'POST' and login_form.is_valid():
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user:
#             auth.login(request, user)
#             form = PostForm()
#             context = {'post_form': form}
#             return render(request, 'postsapp/index.html', context)
#     context = {'title': title, 'login_form': login_form}
#     return render(request, 'postsapp/login.html', context)

class LoginView(TemplateView):
    template_name = "postsapp/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                form = PostForm()
                context['post_form'] = form
                return render(request, 'postsapp/index.html', context)
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            blog = Blog.objects.filter(author=request.user).first()
            form.instance.blog = blog
            form.save()
            subscribers = Subscription.objects.filter(source=blog, is_active=True).select_related()
            addressee_list = []
            for subscriber in subscribers:
                addressee = subscriber.subscriber
                addressee_list.append(addressee.email)
            sender = request.user
            post = Post.objects.filter(blog=blog).last()
            pk = post.pk
            send_newpost_mail(sender, addressee_list, pk)
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


def lenta_news(request):
    lenta_news = {}
    subscriptions = Subscription.objects.filter(subscriber=request.user, is_active=True)
    for item in subscriptions:
        lenta = Post.objects.filter(blog=item.source)
        lenta = sorted(lenta, key=lambda x: x.date_created, reverse=True)
        lenta_news[item.source] = lenta
    context = {
        'lenta': lenta_news
        }
    return render(request, 'postsapp/lenta_news.html', context)


class PostRead(DetailView):
   model = Post

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'пост/просмотр'
       return context

