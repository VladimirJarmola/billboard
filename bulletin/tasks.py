from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Ans


@shared_task
def send_notifications(user, text, pk):
    """Функция отправки сообщений."""
    author_sticker = Ans.objects.filter(pk=pk).values_list(
        'sticker__author__username',
        'sticker__author__email',
        'sticker__heading'
    )

    for username, email, heading in author_sticker:

        html_content = render_to_string(
            'bulletin/ans_create_email.html',
            {
                'text': text,
                'link': f'{settings.SITE_URL}/ans/{pk}',
                'author_sticker': username,
                'heading_sticker': heading,
                'user': user,
            }
        )

        msg = EmailMultiAlternatives(
            subject=heading,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )

        msg.attach_alternative(html_content, 'text/html')

        msg.send()


@shared_task
def send_response_condition(user, email, text, pk):
    """Функция отправки сообщений."""
    author_sticker = Ans.objects.filter(pk=pk).values_list(
        'sticker__author__username',
        'sticker__heading'
    )

    for username, heading in author_sticker:

        html_content = render_to_string(
            'bulletin/ans_condition_email.html',
            {
                'text': text,
                'link': f'{settings.SITE_URL}/ans/{pk}',
                'author_sticker': username,
                'user': user,
            }
        )

        msg = EmailMultiAlternatives(
            subject=heading,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )

        msg.attach_alternative(html_content, 'text/html')

        msg.send()
