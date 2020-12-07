#from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Subscription
from postsapp.models import Blog, Post


def subscribe(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    subscription = Subscription.objects.filter(subscriber=request.user, source=blog).first()
    if not subscription:
        subscription = Subscription(subscriber=request.user, source=blog)
    elif subscription.is_active == False:
        subscription.is_active = True
    else:
        print('Вы уже подписаны')
    subscription.save()
    return HttpResponseRedirect(reverse('subscriptionsapp:my_subscriptions'))


def unsubscribe(request, pk):
    subscription = Subscription.objects.filter(pk=pk).first()
    subscription.is_active = False
    subscription.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UserSubscriptionsList(ListView):
    template_name = "subscriptionsapp/subscriptions.html"
    model = Subscription

    def get_queryset(self):
        return Subscription.objects.filter(subscriber=self.request.user, is_active=True).select_related()


# Create your views here.
