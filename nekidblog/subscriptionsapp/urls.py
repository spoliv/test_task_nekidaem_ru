from django.urls import path
import subscriptionsapp.views as subscriptionsapp



app_name = 'subscriptionsapp'


urlpatterns = [
    path('subscribe/<pk>/', subscriptionsapp.subscribe, name='subscribe'),
    path('unsubscribe/<pk>/', subscriptionsapp.unsubscribe, name='unsubscribe'),
    path('subscriptions/', subscriptionsapp.UserSubscriptionsList.as_view(), name='my_subscriptions'),
    # path('authors/', postsapp.AuthorList.as_view(), name='all_authors'),

]