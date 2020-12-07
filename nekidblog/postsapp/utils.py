from django.core.mail import send_mass_mail
from django.conf import settings
from django.urls import reverse


def send_newpost_mail(sender, addressee_list, pk):
    post_link = reverse('postsapp:post_read', kwargs={
        'pk': pk,
    })

    subject = f'Публикация нового поста {sender.username}'

    message_body = f'Уважаемый подписчик уведомляем Вас, что {sender.username} ' \
        f'опубликовал новый пост в своем блоге. \nДля его просмотра перейдите по ссылке: \n{settings.DOMAIN_NAME}/post/{pk}'
    message = (subject, message_body, settings.EMAIL_HOST_USER, addressee_list)
    return send_mass_mail((message, ), fail_silently=False)
