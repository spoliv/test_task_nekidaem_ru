from django.urls import path
import postsapp.views as postsapp
from django.contrib.auth import urls


app_name = 'postsapp'


urlpatterns = [
    #path('', postsapp.login, name='login'),
    path('', postsapp.LoginView.as_view(), name="login"),
    path('add/', postsapp.CreatePost.as_view(), name='add_post'),
    #path('add/', postsapp.add_post, name='add_post'),
    path('blogs/', postsapp.BlogList.as_view(), name='all_blogs'),
    path('post/<pk>', postsapp.PostRead.as_view(), name='post_read'),
    path('lenta/', postsapp.lenta_news, name='lenta_news'),
    # path('add/', ordersapp.add_order, name='add_order'),
    # path('update/<pk>/', ordersapp.OrderUpdateView.as_view(), name='order_update'),
    # path('delete/<pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
]